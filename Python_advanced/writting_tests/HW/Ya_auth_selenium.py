from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

chrome_driver_path = ChromeDriverManager().install()
browser_service = Service(excutable_path=chrome_driver_path)
browser = webdriver.Chrome(service=browser_service)


def yandex_login(email, password, browser=browser):
    browser.get('https://passport.yandex.ru/auth/')

    email_input = browser.find_element(By.XPATH, '//input[@data-t="field:input-login"]')
    email_input.send_keys(email)
    time.sleep(2)
    email_input.send_keys(Keys.ENTER)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@data-t="field:input-passwd"]'))
    )
    password_input = browser.find_element(By.XPATH, '//input[@data-t="field:input-passwd"]')
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)
    result = browser.title
    browser.close()
    return result


if __name__ == '__main__':
    yandex_login('', '')