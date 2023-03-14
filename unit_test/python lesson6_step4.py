from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)


elements = browser.find_elements(By.XPATH, '//input')

for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
button.click()
time.sleep(30)


button = browser.find_element(By.PARTIAL_LINK_TEXT, '224592')
button.click()
#str(math.ceil(math.pow(math.pi, math.e)*10000))
#button = browser.find_element(By.LINK_TEXT, '224592')
#button = browser.find_element(By.PARTIAL_LINK_TEXT, '224592')



input1 = browser.find_element(By.TAG_NAME, 'input')
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, 'last_name')
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, 'city')
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, 'country')
input4.send_keys("Russia")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
