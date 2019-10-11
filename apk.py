import requests

URL = "https://www.systembolaget.se/api/assortment/products/xml"

response = requests.get(URL)
with open('feed.xml', 'wb') as file:
    file.write(response.content)
