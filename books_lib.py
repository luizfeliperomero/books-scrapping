from colorama import Fore

ARROW_UP = u'\u2191'
ARROW_DOWN = u"\u2193"
TIMES_DASH = 80


def compare_list_of_books(current, previous, currency):
    print("\n")
    for j in range(0, len(current)):
        if(current[j].price_euro > previous[j].price_euro):
            diff = current[j].price_euro - previous[j].price_euro
            percentage = calculate_percentage(diff, previous[j].price_euro)
            info = current[j].name + " : " + Fore.YELLOW + currency.value + str(previous[j].price_euro) + Fore.BLUE + " --> " + Fore.GREEN + currency.value + str(current[j].price_euro) + Fore.RESET + " | " + Fore.CYAN + str(percentage) + "%" + Fore.GREEN + ARROW_UP + Fore.RESET

            print(info)
            print("-" * TIMES_DASH)

        elif(current[j].price_euro < previous[j].price_euro):
            diff = previous[j].price_euro - current[j].price_euro
            percentage = calculate_percentage(diff, previous[j].price_euro)
            info = current[j].name + " : " + Fore.YELLOW + currency.value + str(previous[j].price_euro) + Fore.BLUE + " --> " + Fore.RED + currency.value + str(current[j].price_euro) + Fore.RESET + " | " + Fore.CYAN + str(percentage) + "%" + Fore.RED + ARROW_DOWN + Fore.RESET

            print(info)
            print("-" * TIMES_DASH)

        else:
            info = current[j].name + " : " + Fore.YELLOW + currency.value + str(previous[j].price_euro) + Fore.BLUE + " --> " + Fore.RESET + currency.value + str(current[j].price_euro)

            print(info)
            print("-" * TIMES_DASH)


def calculate_percentage(value, total):
    return round((value / total) * 100, 2)


def add_first_prices(prices, books):
    for i in range(0, len(books)):
        books[i].first_price = prices[i]
        
