#define Path
from pathlib import Path
from tiktokSeleniumAPI.tools import *
path = Path("app/tiktokSeleniumAPI/")

def loginMail(driver,myUsername,myPassword):
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


def loginFaceBook(driver,myUsername,myPassword,typeSpeed):
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

def checkIfLoggedIn(driver):
    return not checkIfElementExist(driver,"//button[contains(text(),'Log in')]")