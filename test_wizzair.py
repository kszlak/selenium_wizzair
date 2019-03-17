# -*- coding: utf-8 -*-
#import bibliotek
from selenium import webdriver
import unittest
import time

valid_name = 'Ola'
valid_lastname = 'Kowalska'

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get("https://wizzair.com/pl-pl#/")

    def tearDown(self):
        self.driver.quit()

    def test_wrong_email(self):
        driver = self.driver
        #zaloguj = driver.find_element_by_css_selector(
        #'#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button')

        zaloguj = driver.find_element_by_xpath(
        '//button[@data-test="navigation-menu-signin"]')
        zaloguj.click()
        time.sleep(3)
        rejestracja = driver.find_element_by_xpath(
        '//button[text()="Rejestracja"]')
        rejestracja.click()
        time.sleep(3)
        imie_field = driver.find_element_by_name('firstName')
        imie_field.send_keys(valid_name)
        time.sleep(3)
        nazwisko_field = driver.find_element_by_xpath(
        '//input[@placeholder="Nazwisko"]')
        nazwisko_field.send_keys(valid_lastname)
        time.sleep(3)
        gender_f_field = driver.find_eleement_by_xpath(
        '//span[text()=" Kobieta "]')
        gender_f_field.click()
        time.sleep(3)
        telnumber_field



if __name__ == '__main__':
    unittest.main(verbosity=2)
