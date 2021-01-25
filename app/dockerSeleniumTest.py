from tiktokSeleniumAPI.TikTokDriver import *

from time import sleep

from pyvirtualdisplay import Display


display = Display(visible=0, size=(1920, 1080))
display.start()



ttapi = TikTokDriver(username,password)
print('driver launched')

print('Driver launched')
# go to Google and click the I'm Feeling Lucky button


if ttapi.checkIfLoggedIn():
    print('User already logged in')
else:
    print('Start login')
    if(ttapi.loginMethod=='facebook'):
        ttapi.loginFaceBook()