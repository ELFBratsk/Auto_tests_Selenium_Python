import pytest
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_page_view(browser):
    browser.get(link)
    time.sleep(10)
    add_to_basket = browser.find_element_by_css_selector('#add_to_basket_form button.btn-add-to-basket') # Селектор кнопки является уникальным для проверяемой страницы ИЛИ так: browser.find_elements_by_css_selector("button.btn.btn-add-to-basket")
    assert add_to_basket, 'Button AddToBasket not found!' # при пустом массиве тест падает