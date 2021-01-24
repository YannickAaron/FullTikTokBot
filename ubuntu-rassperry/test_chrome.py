from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from bs4 import BeautifulSoup

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()

url = 'https://www.google.de'
options = Options()  
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument('--headless')
driver = webdriver.Chrome()
driver.implicitly_wait(60)
print('Driver started successfully')
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')
driver.get_screenshot_as_file("capture_chrome.png")
driver.quit()
