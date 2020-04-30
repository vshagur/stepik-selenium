import os

from selenium import webdriver

from selenium_course.user import User

path_to_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'example.txt')

link = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector('input[name="firstname"]').send_keys(User.name)
browser.find_element_by_css_selector('input[name="lastname"]').send_keys(User.last_name)
browser.find_element_by_css_selector('input[name="email"]').send_keys(User.email)
browser.find_element_by_id('file').send_keys(path_to_file)

browser.find_element_by_css_selector('button.btn').click()

# print answer
print(browser.switch_to.alert.text)

browser.quit()
