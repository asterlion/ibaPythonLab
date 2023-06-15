import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains



class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Chrome()

    def test_social_web(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org
        driver.get("https://www.python.org")
        # проверка наличия слова Python в заголовке страницы
        self.assertIn("Python", driver.title)
        time.sleep(5)
        elem = driver.find_element(By.CLASS_NAME, "winkwink-nudgenudge")
        ActionChains(driver) \
            .move_to_element(elem) \
            .perform()
        time.sleep(5)
        twit = driver.find_element(By.CLASS_NAME, "icon-twitter")
        twit.click()
        time.sleep(5)
        self.assertIn("@ThePSF", driver.page_source)
        time.sleep(5)

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
