from requests import get
from pprint import PrettyPrinter

API_KEY = 'fab5f98d475af45381a46a39'

printer = PrettyPrinter()

def get_currencies():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    data = get(url).json()

    return data["conversion_rates"]

def print_currencies(currencies):
    print("Available currencies:\n")

    for code in sorted(currencies.keys()):
        print(code)

def exchange_rate(currencies, currency1, currency2, amount):
    currency1 = currency1.upper()
    currency2 = currency2.upper()

    if currency1 not in currencies:
        print(f"Currency '{currency1}' not found.")
        return
    
    if currency2 not in currencies:
        print(f"Currency '{currency2}' not found.")
        return
    
    rate1 = currencies[currency1]
    rate2 = currencies[currency2]

    converted_amount = amount * (rate1 / rate2)
    print(f"\n{amount:.2f} {currency1} = {converted_amount:.2f} {currency2}")

def main():
    currencies = get_currencies()
    print_currencies(currencies)

    currency1 = input("\nFrom currency: ")
    currency2 = input("To currency: ")
    amount = float(input("Amount: "))

    exchange_rate(currencies, currency1, currency2, amount)

if __name__ == "__main__":
    main()
