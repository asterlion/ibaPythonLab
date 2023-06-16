import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class SelTableka(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://tabletka.by/")
        driver.maximize_window()
        self.assertIn("Поиск лекарств в аптеках Беларуси", driver.title)
        # ждем 3 секунд
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/input")
        # ждем 3 секунд
        time.sleep(3)
        # набор слова chupakabra в найденном элементе
        elem.send_keys("супрастин")
        # ждем 3 секунд
        time.sleep(3)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 3 секунд
        time.sleep(3)
        # проверка наличия строки "No results found."
        # на странице с результатами поиска
        self.assertIn("Супрастин в аптеках Беларуси", driver.page_source)
        time.sleep(3)
        # ждем 3 секунд
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/input")
        time.sleep(3)
        elem.clear()
        # ждем 3 секунд
        time.sleep(3)
        # набор слова pycon в найденном элементе
        elem.send_keys("pharmaceris")
        # ждем 3 секунд
        time.sleep(3)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 3 секунд
        time.sleep(3)
        self.assertIn("Pharmaceris в аптеках Беларуси", driver.page_source)

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
