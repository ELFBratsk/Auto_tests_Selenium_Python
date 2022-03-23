from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x): #Функция для подсчета значение для переменной x.
  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html" #Открыть страницу
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(options=options, executable_path=r'C:\Chromedriver\chromedriver.exe')
    browser.get(link)
    
    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    
    # Нажать на кнопку "Book" 
    browser.find_element_by_id("book").click()
    
    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(str(y))
    browser.find_element_by_id('solve').click()
    
    # считаем данные в сплывающего окна. Добавил от себя
    print(browser.switch_to.alert.text) 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()