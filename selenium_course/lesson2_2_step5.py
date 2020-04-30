import time

from selenium import webdriver

link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_tag_name("button")

# элемент перекрывается другим
# button.click()

# решаем вопрос с перекрытием
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

assert True

time.sleep(10)
browser.quit()
