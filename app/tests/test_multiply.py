import unittest
from app import create_app

class TestMultiplication(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_multiplication(self):
        response = self.client.post('/multiply', json={'num1': 3, 'num2': 4})
        json_data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_data['result'], 12)

    def test_invalid_input(self):
        response = self.client.post('/multiply', json={'num1': 'a', 'num2': 4})
        self.assertEqual(response.status_code, 400)