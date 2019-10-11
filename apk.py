import requests
import xml.etree.ElementTree as ET
import xml.dom.minidom

URL = "https://www.systembolaget.se/api/assortment/products/xml"

response = requests.get(URL)
with open('feed.xml', 'wb') as file:
    file.write(response.content)

tree = ET.parse('feed.xml')
root = tree.getroot()

articles = root.findall('artikel')

for article in articles:
    price = article.find('PrisPerLiter')
    print(price.text)
