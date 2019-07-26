from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')
chest = browser.find_element_by_css_selector('#treasure')

x = int(chest.get_attribute("valuex"))

answer = str(math.log(abs(12*math.sin(x))))
input = browser.find_element_by_css_selector('#answer')
input.send_keys(answer)

browser.find_element_by_css_selector('#robotCheckbox').click()

human_radio = browser.find_element_by_css_selector('#humanRule')
human_checked = human_radio.get_attribute("checked")
assert human_checked == "true", "Human radio is not selected by default"

robot_radio = browser.find_element_by_css_selector('#robotsRule')
robot_checked = robot_radio.get_attribute("checked")
assert robot_checked is None, "Robot radio is selected by default"
robot_radio.click()


browser.find_element_by_css_selector('.btn').click()

time.sleep(4)