import time
import math
import pytest
from selenium import webdriver

url = ['https://stepik.org/lesson/236895/step/1', 
'https://stepik.org/lesson/236896/step/1', 
'https://stepik.org/lesson/236897/step/1'
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1']

answer = math.log(int(time.time()))

@pytest.mark.parametrize('url', [url])
def ufo_challenge(browser, url):
    browser.get(url)
    time.sleep(1)
    browser.find_element_by_css_selector('a.navbar__auth_only_desktop').click()
    mail = browser.find_element_by_id('id_login_email')
    mail.send_keys('koksharova3093@gmail.com')

    password = browser.find_element_by_id('id_login_password')
    password.send_keys('merterbok')
    time.sleep(1)

    browser.find_element_by_class_name('sign-form__btn').click()
    time.sleep(1)
    browser.find_element_by_link_text('Мои курсы').click()
    time.sleep(1)
    browser.find_element_by_link_text('Продолжить').click()
    time.sleep(5)
    browser.execute_script("window.scrollBy(0, 500);")
    time.sleep(10)
    input2 = browser.find_element_by_css_selector('.textarea')
    input2.send_keys(answer)
    time.sleep(10)
    browser.execute_script("window.scrollBy(0, 500);")
    submit = browser.find_element_by_css_selector('.submit-submission')
    submit.click()
    browser.find_element_by_css_selector('.modern-button__footer').click()

    time.sleep(5)
