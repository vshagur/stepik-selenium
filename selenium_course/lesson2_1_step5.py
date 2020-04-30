import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    num = browser.find_element_by_css_selector('#input_value').text
    answer = calc(int(num))

    browser.find_element_by_css_selector('#answer').send_keys(answer)
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    browser.find_element_by_css_selector("button.btn").click()
    # print answer
    print(browser.switch_to.alert.text)
finally:
    browser.quit()
