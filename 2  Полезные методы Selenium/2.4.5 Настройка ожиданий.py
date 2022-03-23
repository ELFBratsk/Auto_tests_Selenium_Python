from selenium import webdriver
#import time
#import os
#import math

#def calc(x): #Функция для подсчета значение для переменной x.
#  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу http://suninjuly.github.io/cats.html
try: 
    link = "http://suninjuly.github.io/cats.html" #Открыть страницу
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(options=options, executable_path=r'C:\Chromedriver\chromedriver.exe')
    browser.get(link)
    
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get(link)

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text 
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()