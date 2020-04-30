import pytest
from selenium import webdriver

from selenium_course.user import User


class RegistrationPage:
    def __init__(self, browser, link):
        self.browser = browser
        self.browser.get(link)

    def register(self, name, last_name, email):
        self.browser.find_element_by_css_selector('.first_block .first').send_keys(name)
        self.browser.find_element_by_css_selector('.first_block .second').send_keys(
            last_name)
        self.browser.find_element_by_css_selector('.first_block .third').send_keys(email)
        self.browser.find_element_by_css_selector('button.btn').click()


LINKS = [
    'http://suninjuly.github.io/registration1.html',
    'http://suninjuly.github.io/registration2.html'
]

CORRECT_MESSAGE = 'Congratulations! You have successfully registered!'


@pytest.fixture(scope='module')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', LINKS)
def test_correct_registration_page(browser, link):
    """test registration"""

    RegistrationPage(browser, link).register(User.name, User.last_name, User.email)
    message = browser.find_element_by_tag_name("h1").text
    assert message == CORRECT_MESSAGE
