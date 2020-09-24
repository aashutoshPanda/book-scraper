from utils import get_rating
from bs4 import BeautifulSoup
import requests

page_url = "http://books.toscrape.com/catalogue/in-her-wake_980/index.html"
page = requests.get(page_url)
soup = BeautifulSoup(page.content, 'html.parser')

# getting category of book
category_block = soup.find_all('ul', class_='breadcrumb')[0]
category = category_block.find_all('li')[2].get_text()

description_article = soup.find_all('article', class_='product_page')[0]
description_paragraphs = description_article.find_all('p')

price = float(description_paragraphs[0].get_text()[1:])
description = description_paragraphs[3].get_text()
rating = get_rating(description_paragraphs[2]['class'][1])
print(price, description, rating)
