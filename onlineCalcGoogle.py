import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class GoogleTestCalc(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        driver.maximize_window()
        self.assertIn("Google", driver.title)
        # ждем 3 секунд
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
        # ждем 3 секунд
        time.sleep(3)
        # набор слова chupakabra в найденном элементе
        elem.send_keys("онлайн калькулятор")
        # ждем 3 секунд
        time.sleep(3)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div")
        elem.click()
        elem.click()
        elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[4]/div/div")
        elem.click()
        elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div")
        elem.click()
        elem.click()
        elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[4]/div/div")
        elem.click()
        elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div")
        elem.click()
        elem.click()
        elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div")
        elem.click()
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div/span")
        self.assertIn("506", driver.page_source)

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
