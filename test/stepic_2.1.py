"""
https://stepik.org/lesson/165493/step/7?auth=login&unit=140087
Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.set_window_size(1024, 768)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = "http://suninjuly.github.io/get_attribute.html"
# 2.1663022983118063


link = url
browser.get(link)

treasure = browser.find_element(By.ID, 'treasure')
value = treasure.get_attribute('valuex')

new_value = calc(value)

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(new_value)

check_box = browser.find_element(By.ID, 'robotCheckbox')
check_box.click()

radio_button = browser.find_element(By.ID, 'robotsRule')
radio_button.click()

submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_btn.click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
browser.close()
