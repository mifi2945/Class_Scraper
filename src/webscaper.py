from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

import time

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

COURSES = ['PHL 3102']
wish_list = driver.find_element(By.ID, "wishlist-wishlist")
wish_list.send_keys(COURSES)

driver.find_element(By.CLASS_NAME, "msoe-submit-button").click()

time.sleep(60)