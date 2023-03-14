import unittest
import requests
"""
https://playground.learnqa.ru/api/user/login
"""

class TestPlaygroundAPI(unittest.TestCase):
    def test_login_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        url = 'https://playground.learnqa.ru/api/user/login'
        response = requests.post(url, data=data)

        auth_sid = response.cookies["auth_sid"]
        token = response.headers['x-csrf-token']

        # print(response.headers)
        print(response.cookies["auth_sid"])

