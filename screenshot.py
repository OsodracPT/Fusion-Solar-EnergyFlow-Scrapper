from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException        

import config
import sys

options = Options()

# Set headless to False for debugging purposes
options.headless = True
options.add_argument('ignore-certificate-errors')

# RaspberryPi config
# driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)

# Windows webdriver config
driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe', options=options)

# The overview URL of my station
driver.get('https://eu5.fusionsolar.huawei.com/pvmswebsite/assets/build/index.html#/station/overview/NE=34130992')

delay = 3 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'username')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

driver.implicitly_wait(5)

try:
    if driver.find_element_by_id("verificationCodeInput"):
        print("Captcha found. Cant continue!")
        print("Exiting program...")
        driver.quit()
        sys.exit()
    else:
        print("CAPTCHA not found!")
except NoSuchElementException:
    print("CAPTCHA not found!")


#Login
username_element = driver.find_element_by_id("username")
password_element = driver.find_element_by_id("value")

username_element.send_keys(config.username)
password_element.send_keys(config.password)

#Submit credentials and try to login
login_click = driver.find_element_by_id("submitDataverify")
driver.execute_script("arguments[0].click();", login_click)

# Wait for page to load
driver.implicitly_wait(5)

# Close welcome window
try:
    driver.find_element_by_id("login_info_win_close").click()
except NoSuchElementException:
    print("Welcome window not found. Moving on.")

# now that we have the preliminary stuff out of the way time to get that image :D
# find part of the page you want image of
element = driver.find_element_by_class_name('nco-station-overview-energyFlow') 
element.screenshot('painel.png')
driver.quit()
