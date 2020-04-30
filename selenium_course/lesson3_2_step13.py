import unittest

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


class TestRegistration(unittest.TestCase):
    """check registration"""

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(5)
        cls.correct_message = 'Congratulations! You have successfully registered!'

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_correct_registration_page(self):
        """test registration on a valid page"""

        link = 'http://suninjuly.github.io/registration1.html'

        RegistrationPage(self.browser, link).register(
            User.name, User.last_name, User.email)
        message = self.browser.find_element_by_tag_name("h1").text

        self.assertEqual(message, self.correct_message)

    def test_not_correct_registration_page(self):
        """test registration on a invalid page"""

        link = 'http://suninjuly.github.io/registration2.html'

        RegistrationPage(self.browser, link).register(
            User.name, User.last_name, User.email)
        message = self.browser.find_element_by_tag_name("h1").text

        self.assertEqual(message, self.correct_message)


if __name__ == '__main__':
    unittest.main()
