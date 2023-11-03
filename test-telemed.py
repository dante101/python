#!/bin/python3

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()


# url = "irida11"
url = "https://"
service = Service(executable_path="/home/user/python/chromedriver/chromedriver")
browser = webdriver.Chrome(service=service,  options=options)
# browser.set_window_size(480, 320)
browser.maximize_window()
browser.implicitly_wait(5)

try:
    browser.get(url=url)
    time.sleep(2)
    input_login = browser.find_element(By.ID, "signinInputLoginID")
    input_login.clear()
    input_login.send_keys("")
    input_password = browser.find_element(By.ID, "signinInputPasswordID")
    input_password.clear()
    input_password.send_keys("")
    browser.get_screenshot_as_file('login.jpg')
    input_password.send_keys(Keys.ENTER)
    time.sleep(2)
    select = Select(browser.find_element(By.NAME, 'role'))
    select.select_by_visible_text('Суперадминистратор')
    button_enter = browser.find_element(By.ID, 'signinButtonConfirmID')
    button_enter.send_keys(Keys.ENTER)
    click_messages = browser.find_element(
        By.XPATH, "/html/body/div[5]/div[1]/div/ul/li[2]/a").click()
    browser.set_page_load_timeout(30)
    time.sleep(2)
    browser.get_screenshot_as_file('messages.png')
    click_accounts = browser.find_element(
        By.XPATH, "/html/body/div[5]/div[1]/div/ul/li[9]/a").click()
    time.sleep(1)
    browser.get_screenshot_as_file('accounts.png')
    click_forms = browser.find_element(
        By.XPATH, "/html/body/div[5]/div[1]/div/ul/li[10]/a").click()
    time.sleep(1)
    browser.get_screenshot_as_file('forms.png')
    browser.implicitly_wait(5)
    time.sleep(1)
    click_organizations = browser.find_element(
        By.XPATH, "/html/body/div[5]/div[1]/div/ul/li[11]/a").click()
    time.sleep(1)
    browser.get_screenshot_as_file('organizagions.png')
    click_processes = browser.find_element(
        By.XPATH, "/html/body/div[5]/div[1]/div/ul/li[12]/a").click()
    time.sleep(1)
    browser.get_screenshot_as_file('processes.png')
except Exception as ex:
    print("an Exception has occured")
finally:
    browser.close()
    browser.quit()
