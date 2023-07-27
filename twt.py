from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime

''' GLOBAL VARIBALES '''
# Define the path to ChromeDriver executable
PATH = r"C:\Users\SA_SRIT\Downloads\chromedriver-win32.zip\chromedriver-win32\chromedriver.exe"

# Create ChromeOptions
options = Options()
options.add_argument("--start-maximized")  # Optional: To start the browser maximized

# Initialize ChromeDriver with ChromeOptions
driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)
''' END OF GLOBAL VARIBALES '''

def get_link():
    today = input("\nWhat day is this?: ")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Enter google meet lookup links in dictionary named period
    period = {                                                                                 
        'Sub1' : "link1",              
        'Sub2' : "link2",
        'Sub3' : "link3",
        'Sub4' : "link4",
        'Sub5' : "link5",
        'Sub6' : "link6"  }
    
    # Enter your time table in dictionary named day
    time_table =  {    
                    "mon" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"},
                    "tue" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"},
                    "wed" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"},
                    "thu" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"},
                    "fri" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"},
                    "sat" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"} 
                }
    # This if else ladder returns which subject period it needs to this if else ladder returns which subject period it needs to
    if today in ["mon","tue","wed","thu","fri","sat"]:                                                                                                                                      
        if current_time >= '9:00:00' and current_time <= '10:00:00':
            subject = time_table[today][1]
            link = period [subject]
        elif current_time >= '10:10:00' and current_time <= '11:10:00':
            subject = time_table[today][2]
            link = period [subject]
        elif current_time >= '11:20:00' and current_time <= '12:20:00':
            subject = time_table[today][3]
            link = period [subject]
        elif current_time >= '13:20:00' and current_time <= '14:20:00':
            subject = time_table[today][4]
            link = period [subject]
        elif current_time >= '14:30:00' and current_time <= '15:30:00':
            subject = time_table[today][5]
            link = period [subject]
        else:
            subject = "youtube.com"
            link = period[subject]

    # edit the greet message according to the subjects
    if subject in ["sub1","sub2","sub3"]:                      
        greet = "  Good Morning mam !"
    elif subject in ["sub6","sub5","sub4"]:
        greet = "   Good morning sir!"

    arguements = (link,greet)
        
    join_now(driver, actions, arguments)

def join_now(driver, actions, arguments):
    (link,greet) = arguments
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
        textBox.send_keys(greet)

    finally:
        driver.quit()

if __name__ == '__main__':

    get_link()
