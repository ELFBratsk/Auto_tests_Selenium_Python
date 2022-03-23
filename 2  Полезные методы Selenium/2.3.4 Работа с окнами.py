#Задание: принимаем alert
#В этой задаче вам нужно написать программу, 
# которая будет выполнять следующий сценарий:

from selenium import webdriver
import time
#import os
import math

def calc(x): #Функция для подсчета значение для переменной x.
  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу http://suninjuly.github.io/alert_accept.html
try: 
    link = "http://suninjuly.github.io/alert_accept.html" #Открыть страницу
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(options=options, executable_path=r'C:\Chromedriver\chromedriver.exe')
    browser.get(link)
    
    # Нажать на кнопку
    browser.find_element_by_css_selector('.btn').click()
    # Принять confirm
    browser.switch_to.alert.accept()
        
    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(str(y))
    browser.find_element_by_class_name('btn').click()
    
    # считаем данные в сплывающего окна. Добавил от себя
    print(browser.switch_to.alert.text) 
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()