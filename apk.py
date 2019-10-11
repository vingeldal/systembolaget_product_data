import requests
import xml.etree.ElementTree as ET
import pprint

pp = pprint.PrettyPrinter(indent=4)

response = requests.get("https://www.systembolaget.se/api/assortment/products/xml")
with open('feed.xml', 'wb') as file:
    file.write(response.content)

tree = ET.parse('feed.xml')
root = tree.getroot()

articles = root.findall('artikel')

for article in articles:
    product_name = article.find('Namn').text
    price = article.find('PrisPerLiter').text
    strength = article.find('Alkoholhalt').text
    price_numeric = float(price)
    strength_numeric = float(strength[0:4]) / float(100)
    if(strength_numeric != 0):
        alcohol_price = price_numeric / strength_numeric
    else:
        print('No alcohol?! WTF?!')
    print('Product name: ', product_name, ', Price: ', price, 'Alcohol price: ', alcohol_price)
