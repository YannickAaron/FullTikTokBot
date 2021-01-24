from tiktokSeleniumAPI.driver import *
from tiktokSeleniumAPI.tools import *
from tiktokSeleniumAPI.login import *

from time import sleep

from pyvirtualdisplay import Display

import random
sleepTimes = [2.1, 2.8, 3.2, 1.8,0.8,3.2,1.2]

display = Display(visible=0, size=(1920, 1080))
display.start()

username = '@.com'
password = '-goChiz-'

driver = initDriver(username)
print('driver launched')

wait = WebDriverWait(driver, 10)

print('Driver launched')
# go to Google and click the I'm Feeling Lucky button
driver.get("https://www.tiktok.com")

if checkIfLoggedIn(driver):
    print('User already logged in')
else:
    print('Start login')
    loginFaceBook(driver,username,password,0.2)

sleep(5)
driver.get_screenshot_as_file("NewScreen.png")

driver.quit()
