# Задание: параметризация тестов
'''Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим сценарием действий: '''
import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('list', ["236895", "236896", '236897' , '236898' , '236899' , '236903','236904' ,'236905']  ) #Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров: 

class Test:

    def test_url(self, browser, list):
        
        link = f"https://stepik.org/lesson/{list}/step/1" # открыть страницу
        browser.implicitly_wait(10) # дождаться пока информация на сайте прогрузится. ДЛЯ ВСЕХ ЭТАПОВ
        browser.get(link)
        answer = str(math.log(int(time.time()))) # подсчет числа для ввода в поле ответа
        browser.find_element_by_css_selector(".ember-text-area").send_keys(answer) # ввести правильный ответ 
        browser.find_element_by_css_selector(".submit-submission").click() # нажать кнопку "Отправить" 
        
        # проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
        welcome_text = browser.find_element_by_css_selector(".smart-hints__hint")
        assert "Correct!" in welcome_text.text
    
# ОТВЕТ: 'The owls are not what they seem! OvO'