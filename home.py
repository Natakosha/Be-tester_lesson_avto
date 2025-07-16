import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

popUp =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Do not consent"]')))
if popUp:
    popUp[0].click()
else:
    pass

driver.execute_script("window.scrollBy(0, 600);")

Ruby = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product/selenium-ruby/"]')
Ruby.click()
Rev = driver.find_element_by_css_selector('[href="#tab-reviews"]')
Rev.click()

time.sleep(2)
five = driver.find_element_by_css_selector('.comment-form-rating > p> span > a:nth-child(5)')
five.click()
time.sleep(2)

Rev_nice = driver.find_element_by_css_selector('#comment')
Rev_nice.send_keys("Nice book!")
time.sleep(1)
Name = driver.find_element_by_css_selector('#author')
Name.send_keys("Natali")
time.sleep(1)
email = driver.find_element_by_css_selector('#email')
email.send_keys("email@email.com")
time.sleep(1)

submit = driver.find_element_by_css_selector('#submit')
submit.click()






