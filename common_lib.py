from enum import Enum
from urllib.request import urlopen
import os
import sys
import openai
from colorama import Fore

openai.api_key = sys.argv[1]
Currency = Enum('Currency', {'EUR': '€', 'BRL': 'R$', 'US': '$'})
WEBSITE_URL = 'https://books.toscrape.com/'
EQUALS_CHAR = 20 
SLEEP_INTERVAL = 0.2
Regex = Enum('Regex', {'RATING_3_to_5':'star-rating (Three|Four|Five)'})
UPDATES = 5
OUTPUT_FILES_DIR = "output_files"

def get_html():
    try:
        return urlopen(WEBSITE_URL)
    except URLError as url_error:
        raise Exception(WEBSITE_URL + " is invalid")
    except HttpError as http_error:
        raise Exception(http_error)

def generate_html(books):
    chat_gpt_analysis = get_chat_gpt_analysis()
    html_file = open(os.path.join(OUTPUT_FILES_DIR, "index.html"), "w+")
    html_file.write("<!DOCTYPE html><html lang='pt-br'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta http-equiv='X-UA-Compatible' content='ie=edge'><title>Books Scrapping - Luiz Felipe</title><link rel='stylesheet' href='./styles.css'><link rel='icon' href='./favicon.ico' type='image/x-icon'></head><body><div class='top_bar'><h1>Variação de Preços</h1></div><main class='content'><div class='info'><h2>Livros de 3 a 5 estrelas do site <a href='https://books.toscrape.com'>https://books.toscrape.com</a></h2><div class='analysis'><h3>Análise do ChatGPT</h3><article class='analysis-text'>" + chat_gpt_analysis + "</article></div></div><div class='books'>")

    for book in books:
        html_file.write("<div class='book'><p class='name'>" + book.name + "</p><p class='prices'>" + Currency.EUR.value + str(book.first_price) + " " + u"\u2192" + " " + Currency.EUR.value + str(book.last_price) + "</p><p class='variation'>" + str(book.get_price_variation()) + "</p></div>");

    html_file.write("</main></div></body></html>");
    html_file.close()


def get_chat_gpt_analysis():
    with open(os.path.join(OUTPUT_FILES_DIR, "data.txt"), "r") as file:
        data_file_str = file.read()
    print("Chat GPT está analisando...")
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Os seguintes dados correspondem ao preço de livros ao longo de cinco requisições realizadas previamente: " + data_file_str + ". Escreva uma breve análise sobre a variação de preços."},
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content

    print("Análise completa " + Fore.GREEN + u'\u2713' + Fore.RESET + " (disponível em 'output_files/index.html')")
    file.close()
    return result

