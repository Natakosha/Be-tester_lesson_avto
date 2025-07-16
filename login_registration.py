import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://practice.automationtesting.in/")


popUp =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Do not consent"]')))
if popUp:
    popUp[0].click()
else:
    pass

Acc = driver.find_element_by_css_selector('#menu-item-50')
Acc.click()

email = driver.find_element_by_css_selector('#reg_email')
email.send_keys("email@milo.com")
passw = driver.find_element_by_css_selector('#reg_password')
passw.send_keys("5I89Ytrew32!Jo")
time.sleep(5)

Reg = driver.find_element_by_css_selector('[name="register"]')
Reg.click()
time.sleep(1)
driver.close()

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

popUp =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Do not consent"]')))
if popUp:
    popUp[0].click()
else:
    pass

Acc = driver.find_element_by_css_selector('#menu-item-50')
Acc.click()

email = driver.find_element_by_css_selector('#username')
email.send_keys("email@milo.com")
passw = driver.find_element_by_css_selector('#password')
passw.send_keys("5I89Ytrew32!Jo")
time.sleep(5)
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
time.sleep(2)

Complete_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "nav.woocommerce-MyAccount-navigation >ul >li:nth-child(6) >a"), "Logout"))
assert Complete_text, "Что то пошло не так, кнопки LOGOUT нет."
