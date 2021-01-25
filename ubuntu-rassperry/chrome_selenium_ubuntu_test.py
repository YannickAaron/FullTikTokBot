from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

import numpy as np

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value,OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(software_names=software_names,operating_systems=operating_systems,limit=100)

user_agent = user_agent_rotator.get_random_user_agent()

print('Use of Agent: '+str(user_agent))

from pyvirtualdisplay import Display
display = Display(visible=0, size=(1920, 1080))
display.start()

from time import sleep
import random

sleepTimes = np.linspace(0,4,num=20).tolist()

chrome_options = Options()  
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--incognito")
chrome_options.add_argument("Cache-Control=no-cache")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--dns-prefetch-disable")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-certificate-errors-spki-list")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("window-size=1680,1050")
chrome_options.add_extension("crx/u.crx")
chrome_options.add_extension("crx/protect.crx")
chrome_options.page_load_strategy = 'none'
#chrome_options.add_argument('proxy-server=193.8.56.119:9183')
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options) 
driver.delete_all_cookies()
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.header_overrides = {
    'method' : 'GET',
    'accept-encoding' : 'gzip, deflate, br',
    'referrer': 'https://www.tiktok.com/trending',
    'upgrade-insecure-requests' :  '1',
}
wait = WebDriverWait(driver, 10)

print('Driver launched')
# go to Google and click the I'm Feeling Lucky button
driver.get("https://www.tiktok.com")
sleep(random.choice(sleepTimes))
#click login button

wait.until(EC.number_of_windows_to_be(2))
print('more than one window')

for i in driver.find_elements_by_xpath("//button[contains(text(),'Log in')]"):
    print(i.get_attribute('innerHTML'))

driver.find_elements_by_xpath("//button[contains(text(),'Log in')]")[0].click()
print('Log In Button clicked')
sleep(random.choice(sleepTimes))
wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))
print('Switchted to iFrame_Login')
#iframe_login = driver.find_elements_by_class_name("jsx-2873455137")
sleep(random.choice(sleepTimes))


sleep(random.choice(sleepTimes))

###LOGIN WITH MAIL
"""
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Use phone')]"))).click()
if len(driver.find_elements_by_xpath("//input[contains(@placeholder,'Phone')]"))>0:
    sleep(random.choice(sleepTimes))
    print('Mail Login Found')
    #switch to mail login
    driver.find_elements_by_xpath("//a[contains(text(),'email')]")[0].click()
    print('Switched to EMail Login')
    #validate
    if len(driver.find_elements_by_xpath("//input[contains(@placeholder,'Username')]"))>0:
        print('Email Login Found')

        loginUser_input = driver.find_elements_by_xpath("//input[contains(@placeholder,'Username')]")[0]
        loginPW_input = driver.find_elements_by_xpath("//input[contains(@placeholder,'Password')]")[0]
        for char in tiktok_username:
            sleep(0.8)
            loginUser_input.send_keys(char)

        for char in tiktok_pw:
            sleep(0.6)
            loginPW_input.send_keys(char)

        sleep(random.choice(sleepTimes))
        driver.find_elements_by_xpath("//button[contains(text(),'Log in')]")[0].click()
"""

##LOGIN WITH FACEBOOK

wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Facebook')]"))).click()
wait.until(EC.number_of_windows_to_be(3))
print('PopUpWindow detected')
driver.switch_to.window(driver.window_handles[2])
if len(driver.find_elements_by_xpath("//a[contains(text(),'Accept All')]"))>0:
    print('Cookie Banner Found')
    sleep(random.choice(sleepTimes))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Accept All')]"))).click()
if len(driver.find_elements_by_xpath("//input[contains(@placeholder,'email')]"))>0:
    driver.get_screenshot_as_file("UI.png")
    print('Facebook Login Found: NEW UI')
    #switch to mail login

    loginUser_input = driver.find_elements_by_xpath("//input[contains(@placeholder,'email')]")[0]
    loginPW_input = driver.find_elements_by_xpath("//input[contains(@placeholder,'password')]")[0]
    loginButton = driver.find_elements_by_xpath("//button[contains(@value,'Log')]")[0]
    
elif len(driver.find_elements_by_xpath('//*[@id="email"]'))>0:
    driver.get_screenshot_as_file("UI.png")
    print('Facebook Login Found: OLD UI')
    loginUser_input = driver.find_elements_by_xpath('//*[@id="email"]')[0]
    loginPW_input = driver.find_elements_by_xpath('//*[@id="pass"]')[0]
    loginButton = driver.find_elements_by_xpath('//*[@id="loginbutton"]')[0]
else:
    driver.get_screenshot_as_file("NoLoginFound.png")
    print("Login Not Found")
    
if loginUser_input is not None:
    for char in fb_username:
        sleep(0.3)
        loginUser_input.send_keys(char)

    for char in fb_pw:
        sleep(0.2)
        loginPW_input.send_keys(char)

    sleep(random.choice(sleepTimes))
    loginButton.click()

wait.until(EC.number_of_windows_to_be(2))
print('LoginFrame closed')
driver.switch_to.window(driver.window_handles[0])
print('Switched back to normal')
sleep(5)
driver.get_screenshot_as_file("NewScreen.png")
print("Done")

driver.quit()
display.stop()