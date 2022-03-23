from selenium import webdriver
import math
import time

def calc(x): #Функция для подсчета значение для переменной x.
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html" #Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector('#input_value').text
    x = int(x_element)
    y = calc(x) #Считать значение для переменной x.
    
    browser.execute_script("window.scrollBy(0, 100);") # Проскроллить страницу вниз
    
    answer = browser.find_element_by_css_selector('#answer') # поиск поля для ввода значения x
    answer.send_keys(y) # Ввести ответ в текстовое поле.
        
    checkbox1 = browser.find_element_by_css_selector('#robotCheckbox') # Выбрать checkbox "I'm the robot".
    checkbox1.click()
    
    radiobutton1 = browser.find_element_by_css_selector('#robotsRule') # Переключить radiobutton "Robots rule!".
    radiobutton1.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()