from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.saucedemo.com/")


# class TestStonesGame(unittest.TestCase):


def test_login_title():
    title_from_site = driver.title
    assert title_from_site == 'Swag Labs'
    time.sleep(10)


def test_login_form():
    print('Hooray')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    time.sleep(1)

    password = driver.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
    time.sleep(1)

    button_login = driver.find_element(By.XPATH, "//input[@name='login-button']").click()

    time.sleep(1)

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'We reached another site!'

    driver.quit()
time.sleep(4)
driver.quit()
