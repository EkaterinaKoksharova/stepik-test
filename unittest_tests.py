from selenium import webdriver
import unittest
import time


class TESTS(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector ('div.first_block > div.first_class > .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector ('div.first_block > div.second_class > .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector ('div.first_block > div.third_class > .third')
        input3.send_keys("mail@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!", "Тест 1 - не дошли до приветствия")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector ('div.first_block > div.first_class > .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector ('div.first_block > div.second_class > .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector ('div.first_block > div.third_class > .third')
        input3.send_keys("mail@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt2 = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text2 = welcome_text_elt2.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text2, "Поздравляем! Вы успешно зарегистировались!", "Тест 2 - не дошли до приветствия")

if __name__ == "__main__":
    unittest.main()