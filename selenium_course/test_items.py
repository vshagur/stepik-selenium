from selenium.webdriver.common.by import By

from selenium_course.tools import is_element_on_page


def test_button_add_to_cart_exist(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    assert is_element_on_page(browser, By.CSS_SELECTOR, '#add_to_basket_form > button'), \
        'The Add to Cart button does not exist on the page.'
