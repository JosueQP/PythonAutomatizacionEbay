from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\ChromeDriver\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)



driver.get('https://signup.ebay.com/pa/crte?siteid=0&co_partnerId=0&UsingSSL=1&rv4=1&signInUrl=https%3A%2F%2Fwww.ebay.com%2Fsignin%3Fsgn%3Dreg%26siteid%3D0%26co_partnerId%3D0%26UsingSSL%3D1%26rv4%3D1')

WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.NAME,
                                           'firstname'))) \
        .send_keys('luis')

WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.NAME,
                                           'lastname'))) \
        .send_keys('perez')

WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.NAME,
                                           'Email'))) \
        .send_keys('peredoomar161@gmail.com')

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.NAME,
                                           'password'))) \
    .send_keys('Pa$$w0rd')

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.NAME,
                                         'EMAIL_REG_FORM_SUBMIT' ))) \
    .click()

time.sleep(20)
driver.quit()
