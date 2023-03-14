"""
Открыть страницу https://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
 вы увидите окно с числом. Скопируйте его в поле ниже.
"""
import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://suninjuly.github.io/math.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_login_title():
    selector_value = 'input_value'
    x_element = driver.find_element(By.ID, selector_value)
    x = x_element.text
    y = calc(x)
    field = driver.find_element(By.CSS_SELECTOR, 'input#answer')
    field.send_keys(y)
    # Отметить checkbox "I'm the robot".
    checkbox = driver.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    checkbox.click()
    # Выбрать radiobutton "Robots rule!".
    radiobutton = driver.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    radiobutton.click()
    # Нажать на кнопку Submit.
    submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()
    time.sleep(20)
    # find a number
    # 28.88692580781143



