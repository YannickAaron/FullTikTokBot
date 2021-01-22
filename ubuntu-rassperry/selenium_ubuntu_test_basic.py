#https://medium.com/@stefan.preusler/selenium-firefox-in-python-auf-einem-ubuntu-server-df4abc818853
#use arm version of GECKODRIVER
# "sudo apt install firefox-geckodriver
from selenium import webdriver
from bs4 import BeautifulSoup
url = 'https://www.google.de'
options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10)

driver.get("https://www.tiktok.com")

#click login button
driver.find_elements_by_xpath('//*[@id="main"]/div[1]/div/div[3]/button')[0].click()
print('Log In Button clicked')

driver.get_screenshot_as_file("capture.png")

driver.quit()