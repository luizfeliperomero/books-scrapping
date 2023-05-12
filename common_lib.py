from enum import Enum
from urllib.request import urlopen

Currency = Enum('Currency', {'EUR': '€', 'BRL': 'R$', 'US': '$'})
WEBSITE_URL = 'https://books.toscrape.com/'
EQUALS_CHAR = 20 
SLEEP_INTERVAL = 0.2
Regex = Enum('Regex', {'RATING_3_to_5':'star-rating (Three|Four|Five)'})

def get_html():
    try:
        return urlopen(WEBSITE_URL)
    except URLError as url_error:
        raise Exception(WEBSITE_URL + " is invalid")
    except HttpError as http_error:
        raise Exception(http_error)

