#define Path
from pathlib import Path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep
import random

path = Path("/app/tiktokSeleniumAPI/")

def loginMail(self):
    self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Use phone')]"))).click()
    if len(self.driver.find_elements_by_xpath("//input[contains(@placeholder,'Phone')]"))>0:
        sleep(random.choice(self.sleepTimes))
        print('Mail Login Found')
        #switch to mail login
        self.driver.find_elements_by_xpath("//a[contains(text(),'email')]")[0].click()
        print('Switched to EMail Login')
        #validate
        if len(self.driver.find_elements_by_xpath("//input[contains(@placeholder,'Username')]"))>0:
            print('Email Login Found')

            loginUser_input = self.driver.find_elements_by_xpath("//input[contains(@placeholder,'Username')]")[0]
            loginPW_input = self.driver.find_elements_by_xpath("//input[contains(@placeholder,'Password')]")[0]

            self.clearInput(loginUser_input)
            self.clearInput(loginPW_input)

            self.simulateTyping(loginUser_input,self.username)

            self.simulateTyping(loginPW_input,self.password)

            sleep(random.choice(self.sleepTimes))
            self.driver.find_elements_by_xpath("//button[contains(text(),'Log in')]")[0].click()


def loginFaceBook(self,typeSpeed):
    basicLogin(self)
    self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Facebook')]"))).click()
    self.wait.until(EC.number_of_windows_to_be(3))
    print('PopUpWindow detected')
    self.driver.switch_to.window(self.driver.window_handles[2])
    if self.checkIfElementExist("//a[contains(text(),'Accept All')]"):
        print('Cookie Banner Found')
        sleep(random.choice(self.sleepTimes))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Accept All')]"))).click()
    if self.checkIfElementExist("//input[contains(@placeholder,'email') or contains(@placeholder,'Email')]"):
        print('Facebook Login Found: NEW UI')
        #switch to mail login
        self.driver.get_screenshot_as_file("NoLoginFound.png")
        loginUser_input = self.driver.find_elements_by_xpath("//input[contains(@placeholder,'email') or contains(@placeholder,'Email')]")[0]
        loginPW_input = self.driver.find_elements_by_xpath("//input[contains(@placeholder,'password') or contains(@placeholder,'Password')]")[0]
        loginButton = self.driver.find_elements_by_xpath("//button[contains(@value,'Log')]")[0]
        
    elif self.checkIfElementExist('//*[@id="email"]'):
        print('Facebook Login Found: OLD UI')
        loginUser_input = self.driver.find_elements_by_xpath('//*[@id="email"]')[0]
        loginPW_input = self.driver.find_elements_by_xpath('//*[@id="pass"]')[0]
        loginButton = self.driver.find_elements_by_xpath('//*[@id="loginbutton"]')[0]
    else:
        self.driver.get_screenshot_as_file("NoLoginFound.png")
        print("Login Not Found")
        return False
        
    if loginUser_input is not None:
        self.clearInput(loginUser_input)
        self.clearInput(loginPW_input)

        self.simulateTyping(loginUser_input,self.username,typeSpeed)

        self.simulateTyping(loginPW_input,self.password,typeSpeed)

        sleep(random.choice(self.sleepTimes))
        loginButton.click()
    
    self.driver.get_screenshot_as_file("afterLogin.png")
    self.wait.until(EC.number_of_windows_to_be(2))
    print('LoginFrame closed')
    self.driver.switch_to.window(self.driver.window_handles[0])
    print('Switched back to normal')
    sleep(5)
    self.driver.get_screenshot_as_file("LoginSuccessful.png")
    print("Login succesfull")
    return True

def basicLogin(self):
    self.driver.find_elements_by_xpath("//button[contains(text(),'Log in')]")[0].click()
    print('Log In Button clicked')
    sleep(random.choice(self.sleepTimes))
    self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))
    print('Switchted to iFrame_Login')
    #iframe_login = driver.find_elements_by_class_name("jsx-2873455137")
    sleep(random.choice(self.sleepTimes))

def checkIfLoggedIn(self):
    return not self.checkIfElementExist("//button[contains(text(),'Log')]")