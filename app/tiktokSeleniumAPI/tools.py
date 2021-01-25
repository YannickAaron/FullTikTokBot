from time import sleep
from selenium.webdriver.common.keys import Keys

def checkIfElementExist(self,myXpath):
    if len(self.driver.find_elements_by_xpath(myXpath))>0:
        return True
    else:
        return False

def simulateTyping(self,element,myText,mySpeed):
    for char in myText:
        sleep(mySpeed)
        element.send_keys(char)

def clearInput(self,element):
    element.sendKeys(Keys.CONTROL + "a")
    element.sendKeys(Keys.DELETE)
    element.celar()