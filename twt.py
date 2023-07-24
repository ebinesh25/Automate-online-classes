from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
PATH = "/home/positron/Downloads/chromedriver-linux64"
driver = webdriver.Chrome(PATH)
actions = ActionChains(driver)


driver.get("https://meet.google.com/dve-fjud-dth")
print(driver.title)

# class name for mute button is class="GKGgdd"
# For video mute clas="GOH7Zb"


# search = driver.find_element_by_name("s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

actions.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL) # To mute mic
actions.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL) # To mute camera

join = driver.find_element_by_xpath("//*[text()='Join now']")
join.click()

try:
     main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ow3")))

     list_of_buttons = main.find_elements_by_class("r6xAKc")

     chat = list_of_buttons[3]
     chat.click()

     textBox = main.find_elements_by_class("NiQxf")
     textBox.send_keys("Good Morning Makka")
     
    #  articles = main.find_elements_by_tag_name("article")
    #  for article in articles:
    #     header = article.find_element_by_class_name("entry-sumary")
    #     print (header.text) 
finally:
    driver.quit()
