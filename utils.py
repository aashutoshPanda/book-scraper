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
