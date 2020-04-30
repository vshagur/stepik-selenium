from selenium import webdriver

from selenium_course.user import User

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_tag_name('input').send_keys(User.name)
    browser.find_element_by_name('last_name').send_keys(User.last_name)
    browser.find_element_by_class_name('city').send_keys(User.city)
    browser.find_element_by_id('country').send_keys(User.country)
    browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]").click()
    # print answer
    print(browser.switch_to.alert.text)
finally:
    browser.quit()
