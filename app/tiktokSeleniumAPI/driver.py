#define Path
from pathlib import Path
path = '/app/tiktokSeleniumAPI/'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

def initDriver(username):
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value,OperatingSystem.LINUX.value]

    user_agent_rotator = UserAgent(software_names=software_names,operating_systems=operating_systems,limit=100)

    user_agent = user_agent_rotator.get_random_user_agent()
    #user_agent = 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
    print('Use of Agent: '+str(user_agent))

    chrome_options = Options()  
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument(f""+path+"loginCookies/"+username)
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
    chrome_options.add_argument("window-size=1200,1000")
    chrome_options.add_extension(path + "crx/u.crx")
    chrome_options.add_extension(path + "crx/protect.crx")
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

    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',options=chrome_options) 
    #driver.delete_all_cookies()
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.header_overrides = {
        'method' : 'GET',
        'accept-encoding' : 'gzip, deflate, br',
        'referrer': 'https://www.tiktok.com/trending',
        'upgrade-insecure-requests' :  '1',
    }

    return driver