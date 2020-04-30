from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium_course.tools import calc

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 500).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '$100')
)

browser.find_element_by_css_selector('button#book').click()

num = browser.find_element_by_id('input_value').text
result = calc(num)

browser.find_element_by_css_selector('input#answer').send_keys(result)
browser.find_element_by_css_selector('button#solve').click()

# print answer
print(browser.switch_to.alert.text)

browser.quit()
