import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains



class InstituteIba(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Chrome()

    def test_chage_language(self):
        driver = self.driver
        driver.get("https://www.instituteiba.by/")
        driver.maximize_window()
        self.assertIn("Институт ИТ и Бизнес- Администрирования", driver.page_source)
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/header/div/div[1]/div[3]/div[1]/a")
        time.sleep(3)
        ActionChains(driver) \
            .move_to_element(elem) \
            .perform()
        #time.sleep(3)
        elem.click()
        #time.sleep(3)
        self.assertIn("https://www.instituteiba.by/en/", driver.current_url)
        time.sleep(3)
        elem = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/div/div/div[1]/div/header/div/div[1]/div[2]/div[1]/a")
        #time.sleep(3)
        ActionChains(driver) \
            .move_to_element(elem) \
            .perform()
        #time.sleep(3)
        elem.click()
        time.sleep(3)
        self.assertIn("https://www.instituteiba.by/", driver.current_url)
        time.sleep(3)

    def test_online_pay(self):
        driver = self.driver
        driver.get("https://www.instituteiba.by/")
        driver.maximize_window()
        self.assertIn("Институт ИТ и Бизнес- Администрирования", driver.page_source)
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/header/div/div[1]/div[3]/div[4]/div/a")
        time.sleep(3)
        """ActionChains(driver) \
            .move_to_element(elem) \
            .perform()"""
        #time.sleep(3)
        elem.click()
        self.assertIn("https://www.instituteiba.by/payment/", driver.current_url)
        time.sleep(3)
        elem = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/article/form/div[1]/div[2]/input")
        elem.send_keys('Астрейко Татяьна Михайловна')
        time.sleep(3)
        elem = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/article/form/div[2]/div[2]/input")
        elem.send_keys('Python')
        time.sleep(3)
        elem = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/article/form/div[3]/div[2]/input")
        elem.send_keys('1234')
        time.sleep(3)
        elem = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/article/form/div[4]/div[2]/input")
        elem.send_keys('+375297554817')
        time.sleep(3)
        elem = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/article/form/div[5]/div[2]/input")
        elem.send_keys('astreiko1.22@gmail.com')
        time.sleep(3)
        elem = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/article/form/div[6]/div[2]/select")
        elem.click()
        time.sleep(3)
        elem = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/article/form/div[6]/div[2]/select/option[1]")
        elem.click()
        time.sleep(3)
        elem = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/article/form/div[7]/div[2]/input")
        elem.send_keys('248')
        time.sleep(3)
        #попытка обойти рекапчу
        #elem = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/article/form/div[7]/div[2]/input")
        ActionChains(driver) \
            .move_by_offset(-18, 800) \
            .click()
        #elem.click()
        time.sleep(3)
        elem = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/article/form/div[8]/div/input")
        elem.click()
        time.sleep(3)
        self.assertIn("https://payment.webpay.by/", driver.current_url)


    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
