import unittest
import helpers

class test_helpers(unittest.TestCase):

    #
    # def tearDown(self):
    #     pass

    def test_occurenceOfSymbol(self):
        self.assertEqual(helpers.occurenceOfSymbol('$'),'USD')
        self.assertEqual(helpers.occurenceOfSymbol('USD'), False)

    def test_validateCurrency(self):
        self.assertEqual(helpers.validateCurrency('AUD'),True)
        self.assertEqual(helpers.validateCurrency('Something'), False)

    def test_buildRequest(self):
        self.assertEqual(helpers.validateCurrency('AUD,USD'), 'http://api.fixer.io/latest')
        self.assertEqual(helpers.validateCurrency('AUD'), True)

     # def test_getcurrencyExchangeRates(self):
         # pass


     # def buildRequest(base, symbol):
     #     baseUrl = 'http://api.fixer.io/latest'
     #     url = (baseUrl + '?base=' + base)
     #     if symbol:
     #         url += ('&symbols=' + symbol)
     #     return url
     #

# def getcurrencyExchangeRates(base, symbol):
#     url = buildRequest(base, symbol)
#     try:
#         response = requests.get(url)
#         response.status_code
#     except requests.exceptions.HTTPError:
#         print('Error occured while downloading Exchange rates')
#     except requests.exceptions.URLError:
#         print('Error occured while downloading Exchange rates')
#     currencyExchangeRatesJSON = response.text
#     currencyExchangeRates = json.loads(currencyExchangeRatesJSON)
#     return currencyExchangeRates


if __name__ == '__main__':
    unittest.main()


