import unittest
import converter_helpers

class test_converter_helpers(unittest.TestCase):

    def test_occurenceOfSymbol(self):
        self.assertEqual(converter_helpers.occurenceOfSymbol('$'),'USD')
        self.assertEqual(converter_helpers.occurenceOfSymbol('USD'), False)

    def test_validateCurrency(self):
        self.assertEqual(converter_helpers.validateCurrency('AUD'),True)
        self.assertEqual(converter_helpers.validateCurrency('Something'), False)

    def test_buildRequest(self):
        self.assertEqual(converter_helpers.validateCurrency('AUD,USD'), 'http://api.fixer.io/latest')
        self.assertEqual(converter_helpers.validateCurrency('AUD'), True)

    def test_buildRequest(self):
        result = converter_helpers.buildRequest('USD','$')
        self.assertIn('http://api.fixer.io/latest?base=USD&symbols=$', result)

if __name__ == '__main__':
    unittest.main()


