from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

from pathlib import Path

from time import sleep
import random

import os
from os import listdir
from os.path import isfile, join


def checkIfElementExist(myDriver,myXpath):
    if len(myDriver.find_elements_by_xpath(myXpath))>0:
        return True
    else:
        return False

def simulateTyping(myElement,myText,mySpeed=0.3):
    for char in myText:
        sleep(mySpeed)
        myElement.send_keys(char)


###LOGIN WITH MAIL
def loginMail(myUsername,myPassword):
    global driver
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

            simulateTyping(loginUser_input,myUsername)

            simulateTyping(loginPW_input,myPassword)

            sleep(random.choice(sleepTimes))
            driver.find_elements_by_xpath("//button[contains(text(),'Log in')]")[0].click()


##LOGIN WITH FACEBOOK
def loginFaceBook(myUsername,myPassword,typeSpeed):
    global driver
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Facebook')]"))).click()
    wait.until(EC.number_of_windows_to_be(3))
    print('PopUpWindow detected')
    driver.switch_to.window(driver.window_handles[2])
    if checkIfElementExist(driver,"//a[contains(text(),'Accept All')]"):
        print('Cookie Banner Found')
        sleep(random.choice(sleepTimes))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Accept All')]"))).click()
    if checkIfElementExist(driver,"//input[contains(@placeholder,'email')]"):
        print('Facebook Login Found: NEW UI')
        #switch to mail login

        loginUser_input = driver.find_elements_by_xpath("//input[contains(@placeholder,'email')]")[0]
        loginPW_input = driver.find_elements_by_xpath("//input[contains(@placeholder,'password')]")[0]
        loginButton = driver.find_elements_by_xpath("//button[contains(@value,'Log')]")[0]
        
    elif checkIfElementExist(driver,'//*[@id="email"]'):
        print('Facebook Login Found: OLD UI')
        loginUser_input = driver.find_elements_by_xpath('//*[@id="email"]')[0]
        loginPW_input = driver.find_elements_by_xpath('//*[@id="pass"]')[0]
        loginButton = driver.find_elements_by_xpath('//*[@id="loginbutton"]')[0]
    else:
        driver.get_screenshot_as_file("NoLoginFound.png")
        print("Login Not Found")
        return False
        
    if loginUser_input is not None:
        simulateTyping(loginUser_input,myUsername,typeSpeed)

        simulateTyping(loginPW_input,myPassword,typeSpeed)

        sleep(random.choice(sleepTimes))
        loginButton.click()

    wait.until(EC.number_of_windows_to_be(2))
    print('LoginFrame closed')
    driver.switch_to.window(driver.window_handles[0])
    print('Switched back to normal')
    sleep(5)
    driver.get_screenshot_as_file("NewScreen.png")
    print("Login succesfull")
    return True

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value,OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(software_names=software_names,operating_systems=operating_systems,limit=100)

user_agent = user_agent_rotator.get_random_user_agent()
#user_agent = 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
print(user_agent)
tiktok_username = ''
tiktok_pw = ''

fb_username = ''
fb_pw = ''

username = fb_username
#sudo perl -pi -e 's/cdc_asdjflasutopfhvcZLmcfl_/jlssndhajsdhAshfasjasdfasha/g' chromedriver
#grep "cdc_" chromedriver
#$cdc_asdjflasutopfhvcZLmcfl_
# jlssndhajsdhAshfasjasdfasha

sleepTimes = [2.1, 2.8, 3.2, 1.8,0.8,3.2,1.2]

chrome_options = Options()  
#chrome_options.add_argument("--headless")
chrome_options.add_argument(f"user-data-dir="+username)
chrome_options.add_argument("Cache-Control=no-cache")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--dns-prefetch-disable")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-certificate-errors-spki-list")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("window-size=900,1000")
chrome_options.add_extension("crx/u.crx")
chrome_options.add_extension("crx/protect.crx")
chrome_options.page_load_strategy = 'none'
#https://proxy.webshare.io/proxy/list
wireoptions = {
    'proxy': {
        'http': 'http://jteundgh-dest:ej83jpqoqkc1@45.130.255.198:7220', 
        'https': 'https://jteundgh-dest:ej83jpqoqkc1@45.130.255.198:7220',
        'no_proxy': 'localhost,127.0.0.1' # excludes
    }
}
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

driver = webdriver.Chrome(executable_path='assets/chromedriver_stealth', options=chrome_options) #seleniumwire_options=wireoptions
#driver.delete_all_cookies()
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

#check if user logged in
if not checkIfElementExist(driver,"//button[contains(text(),'Log in')]"):
    print('User already logged in')
else:
    driver.find_elements_by_xpath("//button[contains(text(),'Log in')]")[0].click()
    print('Log In Button clicked')
    sleep(random.choice(sleepTimes))
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))
    print('Switchted to iFrame_Login')
    #iframe_login = driver.find_elements_by_class_name("jsx-2873455137")
    sleep(random.choice(sleepTimes))
    if not loginFaceBook(fb_username,fb_pw,0.2):
        print('Program will be terminated')
        driver.quit()
        import sys
        sys.exit()

sleep(random.choice(sleepTimes))

if checkIfElementExist(driver,"//div[contains(@class, 'upload')]"):
    print('Upload Button Found')
    driver.find_elements_by_xpath("//*[contains(@class, 'upload')]")[0].click()

    wait.until(EC.presence_of_element_located((By.XPATH,"//input[contains(@name,'upload')]")))
    
    path = str(Path(__file__).parent.absolute())
    uploadInput = driver.find_element_by_xpath("//input[contains(@name,'upload')]")
    sleep(random.choice(sleepTimes))

    #get list with files

    filesForUpload = [f for f in listdir('readyForUpload/') if isfile(join('readyForUpload/', f)) and join('readyForUpload/', f).endswith('.mp4')]
    print(filesForUpload)
    if(len(filesForUpload)>0):
        print('files Found')
        uploadInput.send_keys(path+'/readyForUpload/'+filesForUpload[0])
        print('use: '+filesForUpload[0])
        sleep(random.choice(sleepTimes))
        sleep(random.choice(sleepTimes))
        captionInput = driver.find_element_by_xpath("//div[contains(@class,'public-DraftStyleDefault-block')]")
        simulateTyping(captionInput,'I hope it made you laugh #funny #fails #fy ',0.2)
        sleep(random.choice(sleepTimes))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Post')]"))).click()
        #driver.find_element_by_xpath("//button[contains(text(),'Post')]").click()
        os.system('mv "readyForUpload/'+filesForUpload[0]+'" usedFiles/')
        print('moved to used: '+filesForUpload[0])
    else:
        print('no files for upload found')


    

#driver.quit()