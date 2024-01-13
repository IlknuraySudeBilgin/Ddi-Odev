from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()

links = []

with open("linkler10.txt", "r", encoding="utf-8") as file:
 links = file.readlines()

for link in links:
    driver.get(link)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "text.font-bold.truncate.text-20")))
    kitapisim = driver.find_element(By.CLASS_NAME, "text.font-bold.truncate.text-20")
    isim = kitapisim.text

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "text-alt")))
    kitaphakkinda = driver.find_element(By.CLASS_NAME, "text-alt")
    hakkinda = " ".join(kitaphakkinda.text.splitlines())
   
    with open("kitaplar.txt", "a", encoding="utf-8") as file:
        file.write(isim + "\n")

    with open("hakkinda.txt", "a", encoding="utf-8") as file:
        file.write(hakkinda + "\n")

    time.sleep(2)