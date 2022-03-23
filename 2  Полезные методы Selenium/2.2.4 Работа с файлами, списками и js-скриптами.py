from selenium import webdriver
#import math
import time
#from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');") # всплывающее popapp 
    time.sleep(2)
    browser.execute_script("document.title='Script executing';alert('Robots at work');") # всплывающее popapp и изменение названия страници
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()