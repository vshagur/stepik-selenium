from selenium import webdriver

from selenium_course.tools import calc

link = 'http://suninjuly.github.io/execute_script.html'

browser = webdriver.Chrome()
browser.get(link)

num = browser.find_element_by_id('input_value').text
result = calc(num)

browser.find_element_by_css_selector('input#answer').send_keys(result)
browser.find_element_by_css_selector('input#robotCheckbox').click()
radio_button = browser.find_element_by_css_selector('input#robotsRule')
browser.execute_script('return arguments[0].scrollIntoView(true);', radio_button)
radio_button.click()

browser.find_element_by_css_selector('button.btn').click()

# print answer
print(browser.switch_to.alert.text)

browser.quit()
