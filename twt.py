
# I edited this in the branch name Implemetation using selenimum
# Hey Now I am editing this from the main branch see whther you can pull this down to you local machine
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "/home/positron/Downloads/chromedriver-linux64"
driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")
print(driver.title)
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)
try:
     main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main")))
     
     articles = main.find_elements_by_tag_name("article")
     for article in articles:
        header = article.find_element_by_class_name("entry-sumary")
        print (header.text)
finally:
    driver.quit()
