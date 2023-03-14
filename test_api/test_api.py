import unittest
import requests
"""
https://breakingbadapi.com/documentation
"""
TARGET_API = "https://www.breakingbadapi.com/api/"
HTTP_OK = 200
TOTAL_CHARACTERS = 62


class TestMyAPI(unittest.TestCase):
    def test_fetch_all_charaters(self):
        response = requests.get(f"{TARGET_API}/characters")
        self.assertEqual(response.status_code, HTTP_OK)
        data = response.json()
        self.assertEqual(
            len(response.json()),
            TOTAL_CHARACTERS,
            f"Failed: expected fetch data: {TOTAL_CHARACTERS} got: {len(response.json())}"
        )

    def test_fetch_all_character_one(self):
        response = requests.get(f'{TARGET_API}characters/1')
        # response = requests.get('https://www.breakingbadapi.com/api/characters/1')
        self.assertEqual(HTTP_OK, response.status_code)
        data = response.text
        print(data)
        data = response.json()
        self.assertEqual(1, len(data))
        self.assertEqual(1, (data[0]['char_id']))
        self.assertEqual("Walter White", data[0]['name'])
        print(response.json())

    def test_fetch_all_auotes_from_a_series(self):
        response = requests.get(f'{TARGET_API}quotes?series=Better+Call+Saul')
        self.assertEqual(HTTP_OK, response.status_code)
        # print(response.json())
        self.assertEqual(
            18,
            len(response.json()),
            'Failed: expecting 18 quotes from Better Call Saul series!'
        )



if __name__ == '__main__':
    unittest.main()