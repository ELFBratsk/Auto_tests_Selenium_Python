#Как работают методы get и find_element
#Разберем еще один простой тест на WebDriver, проверяющий работу кнопки.

#Тестовый сценарий выглядит так:

#Открыть страницу http://suninjuly.github.io/wait1.html
#Нажать на кнопку "Verify"
#Проверить, что появилась надпись "Verification was successful!"
from selenium import webdriver
import time
#import os
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
time.sleep(5)
button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text