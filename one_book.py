from bs4 import BeautifulSoup
import requests

page_url = "http://books.toscrape.com/catalogue/in-her-wake_980/index.html"
page = requests.get(page_url)
soup = BeautifulSoup(page.content, 'html.parser')

# getting category of book
category_block = soup.find_all('ul', class_='breadcrumb')[0]
category = category_block.find_all('li')[2].get_text()

# description_div = soup.find_all('div', id='product_description')
# print(description_div)
