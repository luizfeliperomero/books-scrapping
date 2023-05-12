from urllib.request import urlopen
from bs4 import BeautifulSoup 
from book import Book
from colorama import Fore, Style
import random
import time
import re

from books_lib import compare_list_of_books



WEBSITE_URL = 'https://books.toscrape.com/'
books = []
previous_books = []
EQUALS_CHAR = 20 
file = open("data.txt", "w+")
regex = "star-rating (Three|Four|Five)"
SLEEP_INTERVAL = 0.2

print(('=' * EQUALS_CHAR) + "Books from " + Fore.LIGHTBLUE_EX + WEBSITE_URL + Fore.RESET + ('=' * EQUALS_CHAR) )
print("\n")

for i in range(0, 5):
    try:
        html = urlopen(WEBSITE_URL)
    except URLError as url_error:
        raise Exception(WEBSITE_URL + " is invalid")
    except HttpError as http_error:
        raise Exception(http_error)

    bs = BeautifulSoup(html.read(), 'html.parser')

    try:
        articles = bs.find_all('article', {'class': 'product_pod'})
    except AttributeError as e:
        raise Exception(e)

    if(i > 0):
        print("\n")
        dashes = '─' * 30 
        print(dashes + Style.BRIGHT + "Update─" + Fore.LIGHTYELLOW_EX + str(i) + Fore.RESET + '─' * 40 )


    for b in articles:
        if(re.compile(regex).search(str(b.p))):
            book_name = b.h3.get_text()
            book_price_euro = float(b.h3.find_next_sibling().p.get_text()[1:])

            if(i > 0):
                book_price_euro = round(abs(book_price_euro + random.uniform(-10, 10)), 2)

            book = Book(book_name, book_price_euro)
            books.append(book)
            file.write(book.name + " : " + "€" + str(book.price_euro) + "\n")

            if(i == 0):
                print(book.name + " : " + b.h3.find_next_sibling().p.get_text())
    file.write("-" * 40)
    file.write("\n")
    if(i > 0):
        compare_list_of_books(books, previous_books, "€")


    previous_books = books
    books = []

    time.sleep(SLEEP_INTERVAL)

file.close()
