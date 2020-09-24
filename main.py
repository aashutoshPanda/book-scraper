from bs4 import BeautifulSoup
import requests
from Book import Book


TOTAL_PAGES = 50
for page_no in range(1, TOTAL_PAGES+1):
    page_url = f"http://books.toscrape.com/catalogue/page-{page_no}.html"
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # going through each image-container div to get link for each book
    for image_container in soup.find_all('div', class_='image_container'):
        anchor_tag = image_container.find('a')
        link = anchor_tag['href']
        book = Book(link)
        data = book.get_book_data()
        print(data)
