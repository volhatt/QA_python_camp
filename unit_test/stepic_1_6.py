from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
good_url = "http://suninjuly.github.io/registration1.html"
bad_url = "http://suninjuly.github.io/registration2.html"
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    input1.send_keys('Olga')

    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    input2.send_keys("Ivanova")

    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    input3.send_keys("test@example.com")

    input4 = browser.find_element(By.CSS_SELECTOR, '.second_block .first')
    input4.send_keys("444 444 555")

    input5 = browser.find_element(By.CSS_SELECTOR, '.second_block .second')
    input5.send_keys("Смоленск, улица Иванова, 46")



    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

