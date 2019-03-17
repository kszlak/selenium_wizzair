# -*- coding: utf-8 -*-
#import bibliotek
from selenium import webdriver
import time

#tworzymy nowy sterownik do Chrome
driver = webdriver.Chrome()
#maksymalizuj okno
driver.maximize_window()
#przejdz do strony wsb
driver.get("http://www.wsb.pl")
#poczekaj 3 sek
time.sleep(3)
#wylacz przeglądarke
driver.quit()
