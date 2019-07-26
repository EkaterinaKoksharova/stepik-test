from selenium import webdriver
import math
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name ('firstname')
input1.send_keys("Ivan")
input2 = browser.find_element_by_name ('lastname')
input2.send_keys("Petrov")
input3 = browser.find_element_by_name ('email')
input3.send_keys("mail@mail.ru")

bio = browser.find_element_by_id ('file')
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'bio.txt')           # добавляем к этому пути имя файла 
bio.send_keys(file_path)
browser.find_element_by_css_selector('.btn').click()

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

time.sleep(10)
input2 = browser.find_element_by_css_selector('.textarea')
input2.send_keys(addToClipBoard)
time.sleep(10)
submit = browser.find_element_by_css_selector('.submit-submission')

submit.click()

time.sleep(5)