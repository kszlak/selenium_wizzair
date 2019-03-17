# -*- coding: utf-8 -*-
#import bibliotek
from selenium import webdriver
import unittest

#klasa WsbPLCheck dziedzicząca po klasie unittest
#TestCase z modułu unittest
### SCENARIUSZ TESTOWY ###
class WsbPLCheck(unittest.TestCase):
    #instrukcje wykonujące sie przed każdym testem
    def setUp(self):
        ### WARUNKI WSTĘPNE TESTU ###
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    #instrukcje wykonujące sie po każdym teście
    def tearDown(self):
        ### WARUNKI KOŃCZĄCE TEST ###
        self.driver.quit()

    #Testy zaczynają się od słowa 'test_'
### PRZYPADKI TESTOWE ###
    def test_pierwszy(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        #sprawdzam czy tekst znajduje się w tytule strony
        self.assertIn(u"Wyższe Szkoły Bankowe", driver.title)
        #w pythonie:
        #assert u"Wyższe Szkoły Bankowe" in driver.title
        webelement = self.driver.find_element_by_tag_name('body')
        driver.find_element_by_id('edit-city')
        lupa = driver.find_element_by_class_name('search-icon')
        lupa.click()
        kontakt = driver.find_element_by_partial_link_text('Kont')
        kontakt.click()
        driver.find_element_by_name('city')

    def test_drugi(self):
        pass

    def test_trzeci(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
