import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="choose language")


@pytest.fixture(scope="function")
def browser(request):
    name_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': name_language})
    browser = webdriver.Chrome(options=options)
    
    browser.implicitly_wait(5)
    yield browser
    print(name_language)
    browser.quit()




