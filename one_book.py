from utils import get_nth_page_url, get_price, get_rating, get_stock
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


description = description_paragraphs[3].get_text()
rating = get_rating(description_paragraphs[2]['class'][1])
# print(price, description, rating)


title = soup.find_all('h1')[0].get_text()
print(title)


tds = soup.find_all('td')

UPC = tds[0].get_text()
price_without_tax = get_price(tds[2].get_text())
price_with_tax = get_price(tds[3].get_text())
tax = get_price(tds[4].get_text())
stock = get_stock(tds[5].get_text())
count_reviews = tds[6].get_text()

print(UPC, price_without_tax, price_with_tax, tax, stock, count_reviews)
