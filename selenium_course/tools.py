import math

from selenium.common.exceptions import NoSuchElementException


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def is_element_on_page(webdriver, by, value):
    try:
        webdriver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False
