from flask import Flask
from flask_api import FlaskAPI
import json
import requests
import requests.exceptions
from flask import request

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

app = FlaskAPI('flaskr')
@app.route('/currency_converter')
def currency_converter():
    amount = request.args.get('amount', type = float)
    input = request.args.get('input_currency',  type = str)
    output = request.args.get('output_currency', default= None, type = str)
    if amount == None:
        return("Invalid amount.This field cannot be empty.")
    if occurenceOfSymbol(input):
        input = occurenceOfSymbol(input)
    if occurenceOfSymbol(output):
        output= occurenceOfSymbol(output)
    if validateCurrency(input) == False:
         return("Incorrect input.You must enter valid currency symbol.")
    if (output != None):
        if validateCurrency(output) == False:
            return ("Incorrect output.You must enter valid currency symbol.")
    currencyExchangeRates = getcurrencyExchangeRates(input, output)
    response = {
        'input': {},
        'output': {},
    }
    response['input'] = {
        'amount': amount,
        'currency': input,
    }
    for key, rate in currencyExchangeRates['rates'].items():
        response['output'][key] = round(rate * float(amount),2)
    return response


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False)

