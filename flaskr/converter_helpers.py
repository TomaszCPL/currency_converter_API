# coding=utf-8
import urllib
import json
import requests

def occurenceOfSymbol(symbol):
    listOfSymbols = {'лв':'BGN','R$':'RBL',
        '¥':'CNY','£':'GBP','₪':'ILS','₩':'KRW',
        '₱':'PHP','฿':'THB','$':'USD',}

    if symbol in listOfSymbols:
        return listOfSymbols[symbol]
    else:
        return False

def buildRequest(base, symbol):
    baseUrl = 'http://api.fixer.io/latest'
    url =( baseUrl + '?base=' + base)
    if symbol:
        url +=( '&symbols=' + symbol)
    return url

def validateCurrency(input):
    listOfCurrencies = ['AUD','CAD','CHF',
        'CNY','CZK','DKK','GBP','HKD','HRK','HUF',
        'IDR','ILS','INR','JPY','KRW','MXN','MYR',
        'NOK','NZD','PHP','PLN','RON','RUB','SEK',
        'SGD','THB','TRY','USD']
    if input not in listOfCurrencies:
        return False
    else:
        return True


def getcurrencyExchangeRates(base, symbol):
    url = buildRequest(base, symbol)
    try:
        response = requests.get(url)
        response.status_code
    except requests.exceptions.HTTPError:
        print('Error occured while downloading Exchange rates')
    except requests.exceptions.URLError:
        print('Error occured while downloading Exchange rates')
    currencyExchangeRatesJSON = response.text
    currencyExchangeRates = json.loads(currencyExchangeRatesJSON)
    return currencyExchangeRates

