import unittest
from flaskr import flaskr

class test_flaskApp(unittest.TestCase):
    def setUp(self):
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()

    def test_request_code(self):
        resultFirstCase = self.app.get('/currency_converter?amount=10.92&input_currency=£')
        resultSecondCase = self.app.get('/currency_converter?amount=0.9&input_currency=¥&output_currency=AUD')
        self.assertEqual(resultFirstCase.status_code, 200)
        self.assertEqual(resultSecondCase.status_code, 200)

    def test_wrong_input(self):
        resultInt = self.app.get('/currency_converter?amount=0.9&input_currency=100&output_currency=AUD')
        self.assertIn(b'Incorrect input.You must enter valid currency symbol.', resultInt.data)
        resultEmpty = self.app.get('/currency_converter?amount=0.9&input_currency=&output_currency=AUD')
        self.assertIn(b'Incorrect input.You must enter valid currency symbol.', resultEmpty.data)

    def test_wrong_output(self):
        resultInt = self.app.get('/currency_converter?amount=0.9&input_currency=USD&output_currency=100')
        self.assertIn(b'Incorrect output.You must enter valid currency symbol.', resultInt.data)

    def test_wrong_amount(self):
        result = self.app.get('/currency_converter?amount=&input_currency=£')
        self.assertIn(b'Invalid amount.This field cannot be empty.', result.data)


if __name__ == '__main__':
    unittest.main()
