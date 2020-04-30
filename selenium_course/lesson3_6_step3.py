import math
import time

import pytest
from selenium import webdriver

LINKS = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]


@pytest.fixture(scope='module')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


def send_result(browser, link):
    answer = str(math.log(int(time.time())))
    browser.get(link)
    browser.find_element_by_css_selector(
        'textarea.textarea.string-quiz__textarea.ember-text-area.ember-view').send_keys(
        answer)
    browser.find_element_by_css_selector('button.submit-submission').click()

    return browser.find_element_by_css_selector('pre.smart-hints__hint').text


@pytest.mark.parametrize('link', LINKS)
def test_correct_answer(browser, link):
    assert send_result(browser, link) == 'Correct!'
