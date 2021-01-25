#define Path
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

#def
from .tools import *
from .login import *

path = '/app/tiktokSeleniumAPI/'

class TikTokDriver:

    def __init__(self,username,password,loginMethod='facebook'):

        self.username = username
        self.password = password

        validMethods = ['facebook','email']
        if loginMethod not in validMethods:
            raise Exception('logintMethod not valid')
        else:
            self.loginMethod = loginMethod

        self.sleepTimes = [2.1, 2.8, 3.2, 1.8,0.8,3.2,1.2]

        self.software_names = [SoftwareName.CHROME.value]
        self.operating_systems = [OperatingSystem.WINDOWS.value,OperatingSystem.LINUX.value]

        self.user_agent_rotator = UserAgent(software_names=self.software_names,operating_systems=self.operating_systems,limit=100)

        self.user_agent = self.user_agent_rotator.get_random_user_agent()
        #user_agent = 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
        print('Use of Agent: '+str(self.user_agent))

        self.chrome_options = Options()  
        #chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_argument(f"user-data-dir=/app/tiktokSeleniumAPI/loginCookies/"+self.username)
        self.chrome_options.add_argument("Cache-Control=no-cache")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--dns-prefetch-disable")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--disable-web-security")
        self.chrome_options.add_argument("--ignore-certificate-errors")
        self.chrome_options.add_argument("--ignore-certificate-errors-spki-list")
        self.chrome_options.add_argument("--ignore-ssl-errors")
        self.chrome_options.add_argument("--disable-blink-features")
        self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.chrome_options.add_argument("window-size=1200,1000")
        self.chrome_options.add_extension(path + "crx/u.crx")
        self.chrome_options.add_extension(path + "crx/protect.crx")
        self.chrome_options.page_load_strategy = 'none'
        #https://proxy.webshare.io/proxy/list
        self.wireoptions = {
            'proxy': {
                'http': 'http://jteundgh-dest:ej83jpqoqkc1@45.130.255.198:7220', 
                'https': 'https://jteundgh-dest:ej83jpqoqkc1@45.130.255.198:7220',
                'no_proxy': 'localhost,127.0.0.1' # excludes
            }
        }
        self.chrome_options.add_argument(f"user-agent={self.user_agent}")
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option('useAutomationExtension', False)

        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',options=self.chrome_options) 
        #driver.delete_all_cookies()
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        self.driver.header_overrides = {
            'method' : 'GET',
            'accept-encoding' : 'gzip, deflate, br',
            'referrer': 'https://www.tiktok.com/trending',
            'upgrade-insecure-requests' :  '1',
        }
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.tiktok.com")
        
    
    # Start of tools.py ----------------------------------------

    def simulateTyping(self,myElement,myText,mySpeed=0.3):
        return simulateTyping(self,myElement,myText,mySpeed)

    def checkIfElementExist(self,myXpath):
        return checkIfElementExist(self,myXpath)

    def clearInput(self,element):
        return clearInput(self,element)

    # End of tools.py ----------------------------------------

    # Start of login.py ----------------------------------------

    def loginMail(self):
        return loginMail(self)

    def loginFaceBook(self,typeSpeed=0.2):
        return loginFaceBook(self,typeSpeed)
    
    def checkIfLoggedIn(self):
        return checkIfLoggedIn(self)
    # Start of login.py ----------------------------------------