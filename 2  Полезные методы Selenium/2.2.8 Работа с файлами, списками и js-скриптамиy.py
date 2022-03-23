#Задание: загрузка файла
#В этом задании в форме регистрации требуется загрузить текстовый файл.
#Напишите скрипт, который будет выполнять следующий сценарий:

from selenium import webdriver
import time
import os

#Открыть страницу http://suninjuly.github.io/file_input.html
try: 
    link = "http://suninjuly.github.io/file_input.html" #Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Заполнить текстовые поля: имя, фамилия, email
    browser.find_element_by_name('firstname').send_keys('Vitaliy')
    browser.find_element_by_name('lastname').send_keys('Merzlyakov')
    browser.find_element_by_name('email').send_keys('vitaliy_bratsk@mail.ru')
     

    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element_by_id('file').send_keys(file_path)
    
    #Нажать кнопку "Submit"
    browser.find_element_by_tag_name('button').click()
    
    #Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()