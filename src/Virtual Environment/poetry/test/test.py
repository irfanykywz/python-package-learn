from seleniumbase import Driver
import time

driver = Driver(uc=True, incognito=True)
driver.get("https://nowsecure.nl/#relax")
time.sleep(8)
driver.quit()

# run from terminal
# open  C:\Users\WIN11\AppData\Local\pypoetry\Cache\virtualenvs
# search selenium env
# activate on terminal
# C:\Users\WIN11\AppData\Local\pypoetry\Cache\virtualenvs\seleniumbase-env-aqEimQyq-py3.10\Scripts\activate