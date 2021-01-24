def checkIfElementExist(driver,myXpath):
    if len(driver.find_elements_by_xpath(myXpath))>0:
        return True
    else:
        return False

def simulateTyping(myElement,myText,mySpeed=0.3):
    for char in myText:
        sleep(mySpeed)
        myElement.send_keys(char)