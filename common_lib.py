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
    html_file.write("<!DOCTYPE html><html lang='pt-br'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta http-equiv='X-UA-Compatible' content='ie=edge'><title>My Website</title><link rel='stylesheet' href='./styles.css'><link rel='icon' href='./favicon.ico' type='image/x-icon'></head><body><main class='content'><h1>Variação de Preços</h1><h2>Livros de 3 a 5 estrelas do site <a href='https://books.toscrape.com'>https://books.toscrape.com</a></h2><div class='books'>")

    for book in books:
        html_file.write("<div class='book'><p class='name'>" + book.name + "</p><p class='prices'>" + Currency.EUR.value + str(book.first_price) + " " + u"\u2192" + " " + Currency.EUR.value + str(book.last_price) + "</p><p class='variation'>" + str(book.get_price_variation()) + "</p></div>");

    html_file.write("</main></div></body></html>");
    html_file.close()

