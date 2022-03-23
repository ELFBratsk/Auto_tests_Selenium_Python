from selenium import webdriver
#import math
import time
from selenium.webdriver.support.ui import Select

#def calc(x): #Функция для подсчета значение для переменной x.
# return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects2.html" #Открыть страницу http://suninjuly.github.io/selects1.html
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("#num1")
    y_element = browser.find_element_by_css_selector("#num2")
    x = int(x_element.text) + int(y_element.text) # берем значение и преобразуем в число + Посчитать сумму заданных чисел
    print("Результат",x) # для проверки результата    
    y = str(x) # переводим целочисленное значение в строковое
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y) # Ввести ответ в текстовое поле.
     
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()