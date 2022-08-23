import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from time import sleep

useragent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={useragent.random}')
s = Service(r"E:\Python\autoParsing\chromedriver.exe")
browser = webdriver.Chrome(service=s, options=options)


try:
    url = 'https://www.autodoc.ru/'
    browser.get(url)
    sleep(5)
    browser.find_element(by=By.XPATH, value='//*[@id="loginInfo"]/div/a').click()
    sleep(5)
    email_input = browser.find_element(by=By.XPATH, value='//*[@id="Login"]')

except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()


# print(html)
# for el in html.select(".prc-table prc-table--notepad"):
# title = el.select(".prc-table__row > .prc-table__description")
# print(title.text)
# print(el.text)



