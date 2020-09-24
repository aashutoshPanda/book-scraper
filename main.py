from bs4 import BeautifulSoup
import requests

from utils import get_nth_page_url

count = 0
for page_no in range(1, 51):
    page_url = get_nth_page_url(page_no)
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # going through each image-container div to get link for each book
    for image_container in soup.find_all('div', class_='image_container'):
        anchor_tag = image_container.find('a')
        link = anchor_tag['href']
        print(link)
        count += 1

print(count)
