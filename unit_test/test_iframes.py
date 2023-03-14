import os
import time
import tempfile
import unittest

import http.client as httplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

URL = 'https://techstepacademy.com/iframe-training'


class TestIframesHandling(unittest.TestCase):
    def setUp(self) -> None:
        # initialisation
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.set_window_size(1024, 768)

    def test_iframes_elements(self):
        browser = self.driver
        url = URL
        browser.get(url)

        # to find element inside iframe we need to switch to the iframe
        iframe = browser.find_element(By.CSS_SELECTOR, 'iframe')
        # switch to - and pass an iframe element
        browser.switch_to.frame(iframe)
        welcome_text = browser.find_element(By.CSS_SELECTOR, 'div#block-ec928cee802cf918d26c div p').text

        expected_text = 'Welcome to the Training Ground. The ability find the right Web Elements is crucial to automation,' \
                        ' and a competent engineer can navigate the DOM swiftly and efficiently. Use this space to practice ' \
                        'finding different kinds of elements using CSS Selectors, XPATH, and other methods.'

        self.assertEqual(welcome_text, expected_text)
        # get out from iframe
        browser.switch_to.default_content()
        title_text = browser.find_element(By.CSS_SELECTOR, 'div#block-5d3de848045889000188d389 div p').text
        expected_title = ' Training Ground for IFrames and traditional frames'
        self.assertEqual(expected_title, title_text)


    def tearDown(self) -> None:
        # destroy driver instance
        print('Destroy driver')
        self.driver.quit()
