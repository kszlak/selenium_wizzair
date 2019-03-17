# -*- coding: utf-8 -*-
#import bibliotek
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

valid_name = 'Ola'
valid_lastname = 'Kowalska'
gender = 'male'
valid_phone = '234345555'
invalid_email = 'lalalala.pl'
valid_pass = 'Lalala12!'

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
        zaloguj = WebDriverWait(driver,5).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[data-test=navigation-menu-signin]"
        )))
        #zaloguj = driver.find_element_by_xpath(
        #'//button[@data-test="navigation-menu-signin"]')
        zaloguj.click()
        time.sleep(2)

        rejestracja = driver.find_element_by_xpath(
        '//button[text()="Rejestracja"]')
        rejestracja.click()
        time.sleep(2)
        imie_field = driver.find_element_by_name('firstName')
        imie_field.send_keys(valid_name)

        nazwisko_field = driver.find_element_by_xpath(
        '//input[@placeholder="Nazwisko"]')
        nazwisko_field.send_keys(valid_lastname)

        if gender == 'male':
            m = driver.find_element_by_xpath(
            '//label[@for="register-gender-male"]')
            imie_field.click()
            m.click()
        else:
            f = driver.find_element_by_xpath(
            '//label[@for="register-gender-male"]')
            f.click()

        mobile_field = driver.find_element_by_name("mobilePhone")
        mobile_field.send_keys(valid_phone)

        email_field = driver.find_element_by_xpath(
        '//input[@data-test="booking-register-email"]')
        email_field.send_keys(invalid_email)

        pass_field = driver.find_element_by_xpath(
        '//input[@data-test="booking-register-password"]')
        pass_field.send_keys(valid_pass)

        nation_field = driver.find_element_by_xpath(
        '//input[@data-test="booking-register-country"]')
        nation_field.click()
        nation_to_choose = driver.find_element_by_xpath(
        '//label[@data-test="booking-register-country-label"][164]')
        nation_to_choose.location_once_scrolled_into_view
        nation_to_choose.click()

        privacy_policy = driver.find_element_by_xpath(
        '//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        privacy_policy.click()
        # 11. Kliknij ZAREJESTRUJ
        register_btn = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        register_btn.click()
        time.sleep(3)

        ### TEST ###
        error_notices = self.driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)

        len(visible_error_notices) ==1
        error_text = visible_error_notices[0].get_attribute("innerText")
        print "\n" + error_text
        self.assertEqual(error_text, u"Nieprawidłowy adres e-mail")






if __name__ == '__main__':
    unittest.main(verbosity=2)
