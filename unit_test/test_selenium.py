import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestMePlease(unittest.TestCase):

    new_name = 'bla bla bla'

    def setUp(self) -> None:
        # initialisation
        # print('SetUp test')
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        # self.driver = webdriver.Safari()
        self.driver.set_window_size(1024, 768)

    def test_1(self):
        print('Test 1')
        # test
        url = 'https://www.selenium.dev/about/'
        self.driver.get(url)
        doc_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/documentation']")
        doc_link.click()

        self.assertEqual(self.driver.title, "The Selenium Browser Automation Project | Selenium")
        self.assertEqual(self.driver.current_url, "https://www.selenium.dev/documentation/")

        time.sleep(1)

    def test_2(self):
        print('Test 2')
        # test
        url = 'https://www.selenium.dev/about/'
        self.driver.get(url)
        doc_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/documentation']")
        doc_link.click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @unittest.skip("under development")
    def test_3(self):
        print('Test 2')
        # test
        url = 'https://www.selenium.dev/about/'
        self.driver.get(url)
        doc_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/documentation']")
        doc_link.click()
        time.sleep(5)
        self.driver.execute_script(("window.scrollTo(0, 2500"))



    def tearDown(self) -> None:
        # destroy driver instance
        print('Destroy driver')
        self.driver.close()

if __name__ == '__main__':
    unittest.main()


# to run
# python -m unittest
