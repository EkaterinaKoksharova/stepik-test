from selenium import webdriver
import math
import time
browser = webdriver.Chrome()
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
# time.sleep(3)

browser.get('https://SunInJuly.github.io/execute_script.html')

x = int(browser.find_element_by_css_selector('#input_value').text)

answer = str(math.log(abs(12*math.sin(x))))
input = browser.find_element_by_css_selector('#answer')
input.send_keys(answer)

browser.find_element_by_css_selector('#robotCheckbox').click()
browser.execute_script("window.scrollBy(0, 100);")
browser.find_element_by_css_selector('#robotsRule').click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 500);")
button.click()

#Вставляем ответ в степик
browser.implicitly_wait(3)
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = str(alert_text.split(': ')[-1])
alert.accept()

browser.get('https://stepik.org/')
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
# browser.execute_script("$('html, body').animate({scrollTop: ($('.submit-submission').offset().bottom)},0);")
time.sleep(10)
input2 = browser.find_element_by_css_selector('.textarea')
input2.send_keys(addToClipBoard)
time.sleep(10)
browser.execute_script("window.scrollBy(0, 500);")
submit = browser.find_element_by_css_selector('.submit-submission')
# browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
submit.click()
browser.find_element_by_css_selector('.modern-button__footer').click()

time.sleep(5)

