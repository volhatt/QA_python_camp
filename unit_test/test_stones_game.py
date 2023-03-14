import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestStonesGame(unittest.TestCase):

    def setUp(self) -> None:
        # initialisation
        # print('SetUp test')
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.set_window_size(1024, 768)

    def test_stones(self):
        browser = self.driver
        url = 'https://techstepacademy.com/trial-of-the-stones'
        browser.get(url)

        #  Riddle of Stones
        stone_input = browser.find_element(By.ID, 'r1Input')
        stone_answer_butn = browser.find_element(By.CSS_SELECTOR, 'button#r1Btn')
        stone_result = browser.find_element(By.CSS_SELECTOR, '#passwordBanner>h4')

        #  Riddle of Secrets
        secrets_input = browser.find_element(By.CSS_SELECTOR, "input[id='r2Input']")
        secrets_answer_butn = browser.find_element(By.CSS_SELECTOR, 'button#r2Butn')
        secret_answer = browser.find_element(By.CSS_SELECTOR, "#successBanner1 h4")

        #  Run script
        stone_input.send_keys('rock')
        stone_answer_butn.click()
        password = stone_result.text
        secrets_input.send_keys(password)
        secrets_answer_butn.click()

        secret_answer_text = secret_answer.text

        expected_answer = 'Success!'
        self.assertEqual(expected_answer, secret_answer_text)

        #  Two Merchants
        name_1 = browser.find_element(By.XPATH, "(//div/span/b)[1]").text
        welth_1 = browser.find_element(By.XPATH, "(//div/span/b)[1]/../../p").text

        name_2 = browser.find_element(By.XPATH, "(//div/span/b)[1]").text
        welth_2 = browser.find_element(By.XPATH, "(//div/span/b)[1]/../../p").text

        if int(welth_1) > int(welth_2):
            richest_merchant_name = name_1
        else:
            richest_merchant_name = name_2


        #richest_merchant_name = browser.find_element(By.XPATH, "//p[text()='3000']/../span").text
        merchant_input = browser.find_element(By.ID, 'r3Input')
        merchant_answer_butn = browser.find_element(By.ID, 'r3Butn')
        merchant_result = browser.find_element(By.CSS_SELECTOR, "#successBanner2>h4")
        check_butn = browser.find_element(By.CSS_SELECTOR, "button[name='checkButn']")

        complete_msg = browser.find_element(By.CSS_SELECTOR, "#trialCompleteBanner>h4")

        merchant_input.send_keys(richest_merchant_name)
        merchant_answer_butn.click()

        secret_answer2_text = merchant_result.text
        self.assertEqual(expected_answer, secret_answer2_text)

        check_butn.click()
        expected_complete = 'Trial Complete'
        actual_complete = complete_msg.text
        self.assertEqual(expected_complete, actual_complete)

    def tearDown(self) -> None:
        # destroy driver instance
        print('Destroy driver')
        self.driver.close()
