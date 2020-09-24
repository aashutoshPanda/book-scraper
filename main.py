from bs4 import BeautifulSoup
import requests
import csv
from Book import Book


TOTAL_PAGES = 50
CSV_FILE_NAME = 'book_dataset.csv'
FIELDNAMES = ['title', 'category', 'UPC', 'price_without_tax',
              'price_with_tax', 'tax', 'stock', 'count_reviews', 'rating', 'description']


with open(CSV_FILE_NAME, mode='w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
    writer.writeheader()
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
            writer.writerow(data)
