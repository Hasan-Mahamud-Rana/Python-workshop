# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 00:05:41 2021

@author: 16476
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://www.kijiji.ca/')
SearchKeyword = '//*[@id="SearchKeyword"]'
SearchCategory = '//*[@id="categoryId"]'
search = '//*[@id="MainContainer"]/div[1]/div/div/div/header/div[3]/div/div[2]/form/button[2]'


#driver.find_element_by_xpath(SearchKeyword).send_keys("Student housing")
driver.find_element_by_xpath(search).click()

print(driver.current_url)

import re

myString = "This is my tweet check it out http://example.com/blah"

print(re.search("(?P<url>https?://[^\s]+)", myString).group("url"))

url = driver.current_url
url = url.rsplit('/', 1)[-1]
url = url.rsplit('?', 1)[0]
url

province = 'kitchener'

baseUrl = 'https://www.kijiji.ca/b-real-estate/' + province

baseUrl


s = "256 Phillip St.+Waterloo"
"".join(s.split())
 

txt = '                            3 Bedroom Laurelwood Bungalow for Rent                      '