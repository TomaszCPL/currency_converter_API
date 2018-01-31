from flask_api import FlaskAPI
from flask import request
import converter
from converter_helpers import occurenceOfSymbol, validateCurrency, getcurrencyExchangeRates

app = FlaskAPI('converter')
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

