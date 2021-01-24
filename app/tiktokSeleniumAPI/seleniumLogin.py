#define Path
from pathlib import Path
path = Path("app/tiktokSeleniumAPI/")

from time import sleep
import random

import os
from os import listdir
from os.path import isfile, join

#selenium
from login import loginFaceBook

from tools import *
from driver import initDriver

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

driver = initDriver('tiktok@shareyk.com')
print('driver launched')

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


    

driver.quit()