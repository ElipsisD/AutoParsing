from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from time import sleep
import json
import auth_Auotodoc

useragent = UserAgent()

options = webdriver.ChromeOptions()
options.headless = True  # работа браузера в тихом режиме
options.add_argument('--disable-blink-features-AutomationControlled')  # отключение режима WebDriver
options.add_argument(f'user-agent={useragent.random}')
s = Service(r"E:\Python\autoParsing\chromedriver.exe")


def autodoc_parse(partnumber: str) -> tuple:
    browser = webdriver.Chrome(service=s, options=options)
    browser.get('https://www.autodoc.ru/')
    sleep(2)
    auth(browser)  # авторизация
    finder = browser.find_element(By.XPATH, '//*[@id="partNumberSearch"]')  # окно для ввода номера детали
    finder.clear()
    finder.send_keys(partnumber)  # W7008  2074151  92101-4X000
    finder.send_keys(Keys.ENTER)
    sleep(1)

    """Обработка всплывающего окна"""
    try:
        x = browser.find_element(By.TAG_NAME, 'tbody')
        companies = x.find_elements(By.CLASS_NAME, 'company')
        names = x.find_elements(By.CLASS_NAME, 'particular')
        d_compaies = {}
        for i, (company, name) in enumerate(zip(companies, names), 1):
            d_compaies[i] = (company.text, name.text)
        num, manufacturer, partname = required_manufacturer(d_compaies)
        names[num-1].click()
    except Exception:
        manufacturer, partname = None, None
    finally:
        browser.implicitly_wait(15)
        price = browser.find_element(by=By.TAG_NAME, value='tbody').find_element(by=By.TAG_NAME, value='span').text
        price = int(price.split('.')[0].replace(' ', ''))
        browser.close()
        browser.quit()
    return price, partname, manufacturer


def auth(browser) -> None:
    """Авторизация на сайте"""

    """Вход с вводом логина и пароля"""
    browser.find_element(by=By.XPATH, value='//*[@id="loginInfo"]/div/a').click()
    sleep(2)
    browser.find_element(by=By.XPATH, value='//*[@id="Login"]').send_keys(auth_Auotodoc.login)  # вставляем логин
    browser.find_element(by=By.XPATH, value='//*[@id="Password"]').send_keys(auth_Auotodoc.passw)  # вставляем пароль
    browser.find_element(by=By.XPATH, value='// *[ @ id = "submit_logon_page"]').click()
    sleep(2)
    with open(f'{auth_Auotodoc.login}_cookies', 'w') as fin:
        json.dump(browser.get_cookies(), fin)
    # sleep(3)

    """Вход по заранее сохраненным куки-файлам"""
    # browser.delete_all_cookies()
    # with open(f'{auth_Auotodoc.login}_cookies') as fout:
    #     for cookie in json.load(fout):
    #         browser.add_cookie(cookie)
    # sleep(1)
    # browser.refresh()
    # sleep(1)


def required_manufacturer(manufacturers_options: dict) -> tuple:
    for i, (key, value) in manufacturers_options.items():
        print(f'{i}) {key} \t {value}')
    answer = input('Введите номер нужного варианта: ')
    return int(answer), *manufacturers_options[int(answer)]


# print(autodoc_parse('2074151'))
# print(autodoc_parse('W7008'))
