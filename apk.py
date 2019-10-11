import requests
import xml.etree.ElementTree as ET

URL = "https://www.systembolaget.se/api/assortment/products/xml"

response = requests.get(URL)
with open('feed.xml', 'wb') as file:
    file.write(response.content)

tree = ET.parse('feed.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
