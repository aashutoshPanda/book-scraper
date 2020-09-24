def get_nth_page_url(n):
    """ Makes a book url from given integer"""
    return f"http://books.toscrape.com/catalogue/page-{n}.html"


def get_rating(str_num):
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


def get_stock(str):
    """ gets stock from a text like this
        'In stock (3 available)'    
    """
    stock_str = str.split()[2][1:]
    return int(stock_str)


def get_price(str):
    """ gets float from a string like this
        £11.87 or £0.00
    """
    return float(str[1:])


def get_category(str):
    """ gets category from a string like this
        '\nAutobiography\n'
    """
    return str[1:-1]
