from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(link)

num1 = int(browser.find_element_by_id('num1').text)
num2 = int(browser.find_element_by_id('num2').text)
result = str(num1 + num2)

menu = Select(browser.find_element_by_id('dropdown'))
menu.select_by_value(result)

browser.find_element_by_css_selector("button.btn").click()

# print answer
print(browser.switch_to.alert.text)

browser.quit()
