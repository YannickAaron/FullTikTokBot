
import time
import os

from pathlib import Path
path = Path("app/tiktokSeleniumAPI")
print(path)

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

for i in range(1,10000):
    text = "Hello Docker"
    print(text)
    time.sleep(5)