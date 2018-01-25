import unittest
import helpers

class test_helpers(unittest.TestCase):
    #
    # def setUp(self):
    #     pass
    #
    # def tearDown(self):
    #     pass

    def test_occurenceOfSymbol(self):
        self.assertEqual(helpers.occurenceOfSymbol('$'),'USD')
        self.assertEqual(helpers.occurenceOfSymbol('USD'), False)

    def test_validateCurrency(self):
        self.assertEqual(helpers.validateCurrency('AUD'),True)
        self.assertEqual(helpers.validateCurrency('Something'), False)

    # def test_getcurrencyExchangeRates(self):
    #     pass

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


