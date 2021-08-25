#! python3 
import sys
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()

searchTerm = ' '.join(sys.argv[1:])
driver.get('https://www.google.com/search?q=' + searchTerm)
