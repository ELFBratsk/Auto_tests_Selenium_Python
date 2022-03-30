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


@pytest.mark.parametrize('list', ["236895", "236896", '236897' , '236898' , '236899' , '236903','236904' ,'236905']  )
#@pytest.mark.parametrize('list', ["236895"]  ) Подбирал селекторы на 1 адресе

class Test:

    def test_url(self, browser, list):
        
        link = f"https://stepik.org/lesson/{list}/step/1"
        browser.implicitly_wait(10.05)
        # browser.implicitly_wait(10) # почему то метод .implicitly_wait(10) не сработал.
        browser.get(link)
        time.sleep(8)
        answer = str(math.log(int(time.time())))
        browser.find_element_by_css_selector(".ember-text-area").send_keys(answer)
        browser.find_element_by_css_selector(".submit-submission").click()
        time.sleep(8) 
        welcome_text = browser.find_element_by_css_selector(".smart-hints__hint")
        assert "Correct!" in welcome_text.text
        #browser.find_element(By.CLASS_NAME, 'ember-text-area.ember-view.textarea.string-quiz__textarea').send_keys(answer)

        #browser.find_element(By.CLASS_NAME, 'submit-submission').click()

        #welcome_text = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Correct!" in welcome_text.text
        #time.sleep(5)
        # ОТВЕТ "The owls are not what they seem! OvO"
