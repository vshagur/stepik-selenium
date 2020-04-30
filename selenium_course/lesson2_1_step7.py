from selenium import webdriver

from selenium_course.tools import calc

link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()
browser.get(link)

num = browser.find_element_by_css_selector('#treasure').get_attribute('valuex')
result = calc(num)

browser.find_element_by_css_selector('#answer').send_keys(result)
browser.find_element_by_css_selector('#robotCheckbox').click()
browser.find_element_by_css_selector('#robotsRule').click()
browser.find_element_by_css_selector("button.btn").click()

# print answer
print(browser.switch_to.alert.text)

browser.quit()
