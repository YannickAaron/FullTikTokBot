#https://medium.com/@stefan.preusler/selenium-firefox-in-python-auf-einem-ubuntu-server-df4abc818853
#use arm version of GECKODRIVER
# "sudo apt install firefox-geckodriver
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

from time import sleep
import random

tiktok_username = 'official_failclips'
tiktok_pw = 'Jsk92JsnJ468!'

sleepTimes = [2.1, 2.8, 3.2]

useragent = UserAgent()
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent.random)
profile.set_preference("dom.webdriver.enabled", False)

from bs4 import BeautifulSoup
url = 'https://www.google.de'
options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--headless')
desired_capability = webdriver.DesiredCapabilities.FIREFOX
driver = webdriver.Firefox(options=options,capabilities=desired_capability,firefox_profile=profile)

wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)

print('Driver launched')
# go to Google and click the I'm Feeling Lucky button
driver.get("https://www.tiktok.com")

#click login button

for i in driver.find_elements_by_xpath("//button[contains(text(),'Log in')]"):
    print(i.get_attribute('innerHTML'))

driver.find_elements_by_xpath("//button[contains(text(),'Log in')]")[0].click()
print('Log In Button clicked')

wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))
print('Switchted to iFrame_Login')
#iframe_login = driver.find_elements_by_class_name("jsx-2873455137")

wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Use phone')]"))).click()

sleep(random.choice(sleepTimes))

if len(driver.find_elements_by_xpath("//input[contains(@placeholder,'Phone')]"))>0:
    print('Phone Login Found')
    #switch to mail login
    driver.find_elements_by_xpath("//a[contains(text(),'email')]")[0].click()
    print('Switched to EMail Login')
    #validate
    if len(driver.find_elements_by_xpath("//input[contains(@placeholder,'Username')]"))>0:
        print('Email Login Found')

        driver.find_elements_by_xpath("//input[contains(@placeholder,'Username')]")[0].send_keys(tiktok_username)
        sleep(random.choice(sleepTimes))
        driver.find_elements_by_xpath("//input[contains(@placeholder,'Password')]")[0].send_keys(tiktok_pw)
        sleep(random.choice(sleepTimes))
        driver.find_elements_by_xpath("//button[contains(text(),'Log in')]")[0].click()
driver.get_screenshot_as_file("capture.png")

driver.quit()