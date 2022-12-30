import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    
    unit_price= get_bitcoin_unit_price('USD')
    quantity= number_of_bitcoins(sys.argv[1])

    print(f"${(unit_price * quantity):,.4f}")




def get_bitcoin_unit_price(currency):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Request didn't work.")

    return response.json()['bpi'][currency]["rate_float"]


def number_of_bitcoins(n):
    try:
        number_of_bitcoins = float(n)
    except ValueError:
        print("Command line argument is not a number")
    else:
        return number_of_bitcoins



if __name__ == "__main__":
    main()





