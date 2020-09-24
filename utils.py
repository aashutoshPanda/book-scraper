def get_nth_page_url(n):
    return f"http://books.toscrape.com/catalogue/page-{n}.html"


def get_rating(str_num):
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


def get_stock(str):
    stock_str = str.split()[2][1:]
    return int(stock_str)


def get_price(str):
    return float(str[1:6])
