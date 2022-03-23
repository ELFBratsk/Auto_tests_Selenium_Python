from selenium import webdriver
import math
import time

def calc(x): #Функция для подсчета значение для переменной x.
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html" #Открыть страницу http://suninjuly.github.io/math.html.
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_elements = browser.find_element_by_css_selector('#treasure')
    x_element = x_elements.get_attribute("valuex")
    x = x_element
    y = calc(x) #Считать значение для переменной x.
    answer = browser.find_element_by_css_selector('#answer') # поиск поля для ввода значения x
    answer.send_keys(y) # Ввести ответ в текстовое поле.
    
    checkbox1 = browser.find_element_by_css_selector('#robotCheckbox') # Отметить checkbox "I'm the robot".
    checkbox1.click()
    
    radiobutton1 = browser.find_element_by_css_selector('#robotsRule') # Выбрать radiobutton "Robots rule!".
    radiobutton1.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()