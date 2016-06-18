from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


import unittest


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://facebook.com")


    def test_Login(self):
        driver=self.driver
        emailFieldId="email"
        passFieldId="pass"
        loginButtonXpath="//input[@value='Log In']"
        fblogo="(//a[contains(@href,'logo')])"
        emailFieldElement=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailFieldId))
        passFieldElement=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passFieldId))
        LoginButtonElement=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys('yourusername@somemail.xyz')
        passFieldElement.clear()
        passFieldElement.send_keys('yourpassword')
        LoginButtonElement.click()
        WebdriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(fblogo))


    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
