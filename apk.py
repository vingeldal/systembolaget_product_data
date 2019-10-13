import requests
import sys
import xml.etree.ElementTree as ET

def downloadProductDataToFile():
    response = requests.get("https://www.systembolaget.se/api/assortment/products/xml")
    with open('feed.xml', 'wb') as file:
        file.write(response.content)

def getArticlesFromFile():
    tree = ET.parse('feed.xml')
    root = tree.getroot()

    return root.findall('artikel')

def calculateAlcoholPriceForArticle(article):
    price = article.find('PrisPerLiter').text
    strength = article.find('Alkoholhalt').text
    price_numeric = float(price)
    strength_numeric = float(strength[0:4]) / float(100)
    alcohol_price = price_numeric / strength_numeric

    return alcohol_price

# TODO: Write a function to filter out articles based on parameterized criteria (such as not containing alcohol or not being an "Ekologisk" product)
# TODO: Add a function to sort articles based on a parameterized criteria (like price, alcohol price or packaging)
# TODO: Add unit tests

def main():
    try:
        downloadProductDataToFile()
    except requests.exceptions.RequestException as e:
        print('Failed to download product data from systembolaget')
        print(e)
        sys.exit(1)

    try:
        articles = getArticlesFromFile()
    except:
        print('Failed to open file product data file')
        sys.exit(1)

    for article in articles:
        try:
            alcohol_price_attribute = ET.SubElement(article, 'AlkoholPris')
            alcohol_price_attribute.text = calculateAlcoholPriceForArticle(article)
        except Exception as e:
            print(e)
            name = article.find('Namn').text
            strength = article.find('Alkoholhalt').text
            print('Failed to calculate alcohol price for article: ', name, ', strength: ', strength)

    for article in articles:
        name = article.find('Namn').text
        price = article.find('Prisinklmoms').text
        strength = article.find('Alkoholhalt').text
        if(article.find('AlkoholPris').text):
            alcohol_price = article.find('AlkoholPris').text
            print('Name: ', name, ', Price: ', price, ', Strength: ', strength, ', Alcohol price: ', alcohol_price)

if __name__ == "__main__":
    main()
