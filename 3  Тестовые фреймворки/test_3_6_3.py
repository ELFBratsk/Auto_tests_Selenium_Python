import math
import time
from pip import __main__
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('list', ["236895", "236896", '236897' , '236898' , '236899' , '236903','236904' ,'236905']  )

class Test:

    def test_url(self, browser, list):
        answer = str(math.log(int(time.time())))

        link = f"https://stepik.org/lesson/{list}/step/1"
        browser.get(link)
        time.sleep(5)
        browser.implicity_wait(10)

        browser.find_element(By.CLASS_NAME, 'ember-text-area.ember-view.textarea.string-quiz__textarea').send_keys(answer)

        browser.find_element(By.CLASS_NAME, 'submit-submission').click()

        welcome_text = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Correct!" in welcome_text.text
        time.sleep(5)


if __main__ == __name__:
    pytest.main()