from selenium import webdriver

link = 'http://suninjuly.github.io/huge_form.html'

browser = webdriver.Chrome()
browser.get(link)
result = "Мой ответ"

try:
    elements = browser.find_elements_by_tag_name('input')

    for element in elements:
        element.send_keys(result)

    browser.find_element_by_css_selector("button.btn").click()
    # print answer
    print(browser.switch_to.alert.text)
finally:
    browser.quit()
