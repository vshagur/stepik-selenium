import math

from selenium import webdriver

from selenium_course.user import User

link = "http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_link_text(text).click()
    browser.find_element_by_tag_name('input').send_keys(User.name)
    browser.find_element_by_name('last_name').send_keys(User.last_name)
    browser.find_element_by_class_name('city').send_keys(User.city)
    browser.find_element_by_id('country').send_keys(User.country)
    browser.find_element_by_css_selector("button.btn").click()
    # print answer
    print(browser.switch_to.alert.text)
finally:
    browser.quit()
