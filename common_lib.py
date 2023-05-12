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

def generate_html(books):
    html_file = open("index.html", "w+")
    html_file.write("<!DOCTYPE html><html lang='pt-br'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta http-equiv='X-UA-Compatible' content='ie=edge'><title>My Website</title><link rel='stylesheet' href='./style.css'><link rel='icon' href='./favicon.ico' type='image/x-icon'></head><body><main class='content'><h1>Histórico de Preços</h1><div class='books'>")

    for book in books:
        html_file.write("<div class='book'><p>" + book.name + "<p><p>" + str(book.first_price) + "<p><p>" + str(book.last_price) + "<p></div>");

    html_file.write("</main></div></body></html>");
    html_file.close()

def add_first_prices(prices, books):
    for i in range(0, len(books) - 1):
        books[i].first_price = prices[i]
        
