from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

import time
import argparse
import numpy as np

# set up command line arguments
parser = argparse.ArgumentParser(description="Web scraper for MSOE course registration.")
parser.add_argument('courses', nargs='*', help='Add courses to wishlist in the format: [DEPARTMENT]-[COURSE NUMBER]:[SECTION] (ie MTH-1120:002)')
args = parser.parse_args()

COURSES = []
for entry in args.courses:
    if ':' in entry:
        course, section = entry.split(':', 1)
    else:
        course, section = entry, ''
    COURSES.append({'course': course, 'section': f'{section}\n'})

# debug
print(COURSES)
exit(0)

# set up options
options = ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--log-level=3") #supress most logs
#options.add_argument("--headless") # run in headless mode (no GUI)
#options.add_argument("--no-gpu")

# start Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://resources.msoe.edu/sched/index.php")
driver.implicitly_wait(5)


wish_list = driver.find_element(By.ID, "wishlist-wishlist")
wish_list.send_keys(COURSES)

driver.find_element(By.CLASS_NAME, "msoe-submit-button").click()

# after loading all courses



# debugging, leaves browser open for 60 seconds
time.sleep(60)