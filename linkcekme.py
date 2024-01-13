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

next_page = []
page_num = 2

driver.get("https://1000kitap.com/kitaplar/en-begenilenler")

while True:
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'dr.self-start.max-w-full.flex-row.cursor')))
        links = driver.find_elements(By.CSS_SELECTOR, "a.dr.self-start.max-w-full.flex-row.cursor")

        for i in range(len(links)-3):
            if i < len(links) and links[i].get_attribute("href").startswith("https://1000kitap.com/kitap/"):
                if links[i].is_displayed() and links[i].is_enabled():
                    with open("linkler10.txt", "a", encoding="utf-8") as file:
                        file.write(links[i].get_attribute("href") + "\n")
                else:
                    print(f"")


        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a")))
        pages = driver.find_elements(By.CSS_SELECTOR, "a")
        for page in pages:
            if page.get_attribute("href").endswith(str(page_num)) and page.get_attribute("href").startswith("https://1000kitap.com/kitaplar/en-begenilenler?sayfa="):
                page.click()
                page_num += 1
                time.sleep(5)
                break

    except NoSuchElementException:
        break

driver.quit()