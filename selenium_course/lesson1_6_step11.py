import time

from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"
# link = "http://suninjuly.github.io/registration2.html"

name, last_name, email = 'Ivan', 'Petrov', 'petrov@mail.ru'
expected = "Congratulations! You have successfully registered!"

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

try:
    browser.find_element_by_css_selector('.first_block .first').send_keys(name)
    browser.find_element_by_css_selector('.first_block .second').send_keys(last_name)
    browser.find_element_by_css_selector('.first_block .third').send_keys(email)
    browser.find_element_by_css_selector("button.btn").click()
    welcome_text = browser.find_element_by_tag_name("h1").text
    assert welcome_text == expected
finally:
    time.sleep(10)
    browser.quit()
