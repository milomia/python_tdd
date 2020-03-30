import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox
 
#-- Setup
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=options)
#-- Parse
browser.get('http://I want to enter')
soup = BeautifulSoup(browser.page_source, 'lxml')
welcome = soup.select('head > title')
print(welcome.text)
