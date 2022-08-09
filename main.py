from email import header
from re import S
from requests import Request, Session
import json
import pprint

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
print("BTC Price: $ " + str("${:0,.2f}".format(btcPriceUSD)))
