import json
from bs4 import BeautifulSoup
import requests

URL = "https://books.toscrape.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

book_divs = soup.find_all('article', class_='product_pod')

# create an empty list to store the data
data = []

# loop through the book divs and extract the title and price
for div in book_divs:
    title = div.h3.a['title']
    price = div.find('p', class_='price_color').text
    
    # store the data in a dictionary
    book_data = {
        'title': title,
        'price': price
    }
    
    # add the dictionary to the list
    data.append(book_data)

# open a file and write the data to it in JSON format using UTF-8 encoding
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)
