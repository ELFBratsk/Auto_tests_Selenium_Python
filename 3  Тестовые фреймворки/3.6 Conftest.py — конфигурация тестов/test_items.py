import pytest
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_page_view(browser):
    browser.get(link)
    time.sleep(10)
    add_to_basket = browser.find_element_by_css_selector('#add_to_basket_form button.btn-add-to-basket')
    assert add_to_basket, 'Button "Add to basket" not found.'