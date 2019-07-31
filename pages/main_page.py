from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"