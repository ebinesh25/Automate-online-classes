# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# def join_now(driver,actions,link):
#     driver.get(link)
#     print(driver.title)

#     time.sleep(5)


#     # class name for mute button is class="GKGgdd"
#     # For video mute clas="GOH7Zb"


#     # search = driver.find_element_by_name("s")
#     # search.send_keys("test")
#     # search.send_keys(Keys.RETURN)

#     actions.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL) # To mute mic
#     actions.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL) # To mute camera

#     join = driver.find_element_by_XPATH("//*[text()='Join now']")
#     join.click()

#     try:
#         main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ow3")))

#         list_of_buttons = main.find_elements_by_class("r6xAKc")

#         chat = list_of_buttons[3]
#         chat.click()

#         textBox = main.find_elements_by_class("NiQxf")
#         textBox.send_keys("Good Morning Makka")
        
#         #  articles = main.find_elements_by_tag_name("article")
#         #  for article in articles:
#         #     header = article.find_element_by_class_name("entry-sumary")
#         #     print (header.text) 
#     finally:
#         driver.quit()

# if __name__ == '__main__':
    
# # Define the path to ChromeDriver executable
#     PATH = r"C:\Users\SA_SRIT\Downloads\chromedriver-win32.zip\chromedriver-win32\chromedriver.exe"

#     # Create ChromeOptions
#     options = Options()
#     options.add_argument("--start-maximized")  # Optional: To start the browser maximized

#     # Initialize ChromeDriver with ChromeOptions
#     driver = webdriver.Chrome(options=options)
#     actions = ActionChains(driver)
#     link = "https://meet.google.com/dve-fjud-dth"

#     join_now(driver,actions,link)
    

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def join_now(driver, actions, link):
    driver.get(link)
    print(driver.title)

    time.sleep(15)

    actions.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL)  # To mute mic
    actions.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL)  # To mute camera

    join = driver.find_element(By.XPATH, "//*[text()='Join now']")
    join.click()

    try:
        main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ow3")))

        list_of_buttons = main.find_elements(By.CLASS_NAME, "r6xAKc")

        chat = list_of_buttons[3]
        chat.click()

        textBox = main.find_element(By.CLASS_NAME, "NiQxf")
        textBox.send_keys("Good Morning Makka")

    finally:
        driver.quit()

if __name__ == '__main__':
    # Define the path to ChromeDriver executable
    PATH = r"C:\Users\SA_SRIT\Downloads\chromedriver-win32.zip\chromedriver-win32\chromedriver.exe"

    # Create ChromeOptions
    options = Options()
    options.add_argument("--start-maximized")  # Optional: To start the browser maximized

    # Initialize ChromeDriver with ChromeOptions
    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)
    link = "https://meet.google.com/bep-mnks-gep"

    join_now(driver, actions, link)
