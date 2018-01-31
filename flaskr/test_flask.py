import unittest
from flaskr import flaskr

class test_flaskApp(unittest.TestCase):
    def setUp(self):
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()

    def test_request_code(self):
        resultFirstRoute = self.app.get('/currency_converter/amount=500&input_currency=USD')
        resultSecondRoute = self.app.get('/currency_converter/amount=500&input_currency=USD&output_currency=PLN')
        self.assertEqual(resultFirstRoute.status_code, 200)
        self.assertEqual(resultSecondRoute.status_code, 200)

    # def test_home_data(self):
    #     # sends HTTP GET request to the application
    #     # on the specified path
    #     result = self.app.get('/')
    #     self.assertEqual(result.data, "Hello World!!!")


if __name__ == '__main__':
    unittest.main()
