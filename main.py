from email import header
from re import S
from requests import Request, Session
import json
import pprint
from sys import platform
import os

if platform == "win32":
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

clear()

print("PyCrypto\nCrypto currencies price consulting API:\n\n")

with open('key.txt') as f:
    apiKey = f.readlines()[0]

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'slug':'bitcoin',
    'convert':'USD'
}

headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY': apiKey
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)

btcPriceUSD = json.loads(response.text)['data']['1']['quote']['USD']['price']
print(" - ₿ (BTC): $ " + str("${:0,.2f}".format(btcPriceUSD)))

print("\n\nPress enter to exit.")
input()
