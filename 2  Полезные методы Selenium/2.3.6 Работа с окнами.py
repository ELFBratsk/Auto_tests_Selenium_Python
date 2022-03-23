#В этом задании после нажатия кнопки страница откроется в новой вкладке, 
# нужно переключить WebDriver на новую вкладку и решить в ней задачу.

from selenium import webdriver
import time
#import os
import math

def calc(x): #Функция для подсчета значение для переменной x.
  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
try: 
    link = "http://suninjuly.github.io/redirect_accept.html" #Открыть страницу
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(options=options, executable_path=r'C:\Chromedriver\chromedriver.exe')
    browser.get(link)
    
    # Нажать на кнопку
    browser.find_element_by_css_selector('.trollface.btn').click()
    
    # Переключиться на новую вкладк
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
        
    # Пройти капчу для робота и получить число-ответ
    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(str(y))
    browser.find_element_by_class_name('btn').click()
    time.sleep(5)
    # считаем данные в сплывающего окна. Добавил от себя
    print(browser.switch_to.alert.text) 
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()