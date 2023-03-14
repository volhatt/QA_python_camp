import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#driver.set_window_size(1024, 768)

driver.get("https://www.saucedemo.com/")

def login_title():
    title_from_site = driver.title
    assert title_from_site == 'Swag Labs'
    time.sleep(3)


def test_login_form():
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    time.sleep(1)

    password = driver.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
    time.sleep(1)

    button_login =driver.find_element(By.XPATH, "//input[@name='login-button']").click()

    time.sleep(1)

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'We reached another site!'

    driver.quit()
