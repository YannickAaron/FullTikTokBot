from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pyvirtualdisplay import Display
display = Display(visible=0, size=(1920, 1080))
display.start()

from time import sleep
import random

sleepTimes = [2.1, 2.8, 3.2]

tiktok_username = 'official_failclips'
tiktok_pw = 'hastdugedachtichschreibhiermeinpassworthin!'

chrome_options = Options()  
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
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
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options) 
driver.delete_all_cookies()
#driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
wait = WebDriverWait(driver, 10)

print('Driver launched')
# go to Google and click the I'm Feeling Lucky button
driver.get("https://www.tiktok.com")
driver.get_screenshot_as_file("capture_chrome1.png")
#click login button

for i in driver.find_elements_by_xpath("//button[contains(text(),'Log in')]"):
    print(i.get_attribute('innerHTML'))

driver.find_elements_by_xpath("//button[contains(text(),'Log in')]")[0].click()
print('Log In Button clicked')

wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))
print('Switchted to iFrame_Login')
#iframe_login = driver.find_elements_by_class_name("jsx-2873455137")

wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Use phone')]"))).click()

sleep(random.choice(sleepTimes))

if len(driver.find_elements_by_xpath("//input[contains(@placeholder,'Phone')]"))>0:
    print('Phone Login Found')
    #switch to mail login
    driver.find_elements_by_xpath("//a[contains(text(),'email')]")[0].click()
    print('Switched to EMail Login')
    #validate
    if len(driver.find_elements_by_xpath("//input[contains(@placeholder,'Username')]"))>0:
        print('Email Login Found')

        driver.find_elements_by_xpath("//input[contains(@placeholder,'Username')]")[0].send_keys(tiktok_username)
        sleep(random.choice(sleepTimes))
        driver.find_elements_by_xpath("//input[contains(@placeholder,'Password')]")[0].send_keys(tiktok_pw)
        sleep(random.choice(sleepTimes))
        driver.find_elements_by_xpath("//button[contains(text(),'Log in')]")[0].click()


driver.get_screenshot_as_file("capture_chrome.png")
#stop display and browser
driver.quit()
display.stop()