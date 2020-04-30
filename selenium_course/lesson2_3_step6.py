from selenium import webdriver

from selenium_course.tools import calc

link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector('button.trollface').click()

old_window, new_window = browser.window_handles
browser.switch_to.window(new_window)

num = browser.find_element_by_id('input_value').text
result = calc(num)

browser.find_element_by_css_selector('input#answer').send_keys(result)
browser.find_element_by_css_selector('button.btn').click()

# print answer
print(browser.switch_to.alert.text)

browser.quit()
