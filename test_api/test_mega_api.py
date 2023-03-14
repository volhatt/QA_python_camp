import unittest
import requests
"""
https://jsonplaceholder.typicode.com/
"""
TARGET_API = "https://jsonplaceholder.typicode.com/"
EXPECTED_STATUS = 200
TOTAL_POSTS = 100


class TestMegaAPI(unittest.TestCase):
    def test_get_all_posts(self):
        response = requests.get(f"{TARGET_API}posts")
        self.assertEqual(response.status_code, EXPECTED_STATUS)
        data = response.json()
        self.assertEqual(
            len(data),
            TOTAL_POSTS,
            f"Failed: expected fetch data: {TOTAL_POSTS} got: {len(data)}"
        )

    def test_get_post_1(self):
        response = requests.get(f"{TARGET_API}posts/2")
        self.assertEqual(response.status_code, EXPECTED_STATUS)
        data = response.json()
        self.assertEqual(
            len(data),
            4,
            f"Failed: expected fetch data: 4 got: {len(data)}"
        )
        expected_keys = ['userId', 'id', 'title', 'body']
        actual_keys = list(data.keys())
        for i in range(len(expected_keys)):
            self.assertEqual(expected_keys[i], actual_keys[i])
        print(data['id'])

    def test_post_post(self):
        # create post
        url = f"{TARGET_API}posts"
        payload = {
                'title': 'olga',
                'body': 'bar',
                'userId': 1,
            }
        response = requests.post(url, data=payload)
        data = response.json()
        print(data)
        expected_title = 'olga'
        actual_title = data['title']
        self.assertEqual(expected_title, actual_title)

        # 2. put request
        url = f"{TARGET_API}posts/1"
        payload1 = {
            'body': 'new body',
        }
        response = requests.put(url, data=payload1)
        data = response.json()
        print(data)

    def test_delete(self):
        url = f"{TARGET_API}posts/1"
        response = requests.delete(url)
        self.assertEqual(response.status_code, EXPECTED_STATUS)






if __name__ == '__main__':
    unittest.main()