from bs4 import BeautifulSoup
import requests


class Book:
    def __init__(self, link):
        self.url = self.get_book_url(link)

    def get_nth_page_url(self, n):
        """ makes url from the index """
        return (f"http://books.toscrape.com/catalogue/page-{n}.html")

    def get_rating(self, str_num):
        """ Makes integer rating from the options """
        options = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5,
        }
        try:
            return options[str_num]
        except:
            raise("string not a valid raing ")

    def get_stock(self, str):
        """ gets stock from a text like this
            'In stock (3 available)'    
        """
        stock_str = str.split()[2][1:]
        return int(stock_str)

    def get_price(self, str):
        """ gets float from a string like this
            £11.87 or £0.00
        """
        return float(str[1:])

    def get_category(self, str):
        """ gets category from a string like this
            '\nAutobiography\n'
        """
        return str[1:-1]

    def get_book_url(self, link):
        """ Making a url for a book like this
            http://books.toscrape.com/catalogue/running-with-scissors_215/index.html
        """
        return "http://books.toscrape.com/catalogue/" + link

    def get_book_data(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        """ Category """
        category_block = soup.find_all('ul', class_='breadcrumb')[0]
        category = self.get_category(
            category_block.find_all('li')[2].get_text())

        """ Description & Rating """
        description_article = soup.find_all(
            'article', class_='product_page')[0]
        description_paragraphs = description_article.find_all('p')
        description = description_paragraphs[3].get_text()
        rating = self.get_rating(description_paragraphs[2]['class'][1])

        """ Title """
        title = soup.find_all('h1')[0].get_text()

        """ UPC & other details """
        tds = soup.find_all('td')

        UPC = tds[0].get_text()
        price_without_tax = self.get_price(tds[2].get_text())
        price_with_tax = self.get_price(tds[3].get_text())
        tax = self.get_price(tds[4].get_text())
        stock = self.get_stock(tds[5].get_text())
        count_reviews = tds[6].get_text()

        book_data = {
            'title': title,
            'category': category,
            'UPC': UPC,
            'price_without_tax': price_without_tax,
            'price_with_tax': price_with_tax,
            'tax': tax,
            'stock': stock,
            'count_reviews': count_reviews,
            'rating': rating,
            'description': description
        }
        return book_data
