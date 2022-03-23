from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

#def calc(x): #Функция для подсчета значение для переменной x.
#  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу http://suninjuly.github.io/wait2.html
try: 
    link = "http://suninjuly.github.io/wait2.html" #Открыть страницу
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(options=options, executable_path=r'C:\Chromedriver\chromedriver.exe')
    browser.get(link)
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()