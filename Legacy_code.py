from time import sleep
import webbrowser
from datetime import datetime
import pyautogui as py

a = input("\nWhat day is this?: ")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

period = {                                                                                 # Enter google meet lookup links in dictionary named period
    'Sub1' : "link1",              
    'Sub2' : "link2",
    'Sub3' : "link3",
    'Sub4' : "link4",
    'Sub5' : "link5",
    'Sub6' : "link6"  }
    
day =  {    "mon" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"},   # Enter your time table in dictionary named day
            "tue" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"},
            "wed" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"},
            "thu" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"},
            "fri" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"},
            "sat" : { 1: "sub1", 2: "sub2", 3: "sub3", 4: "sub4", 5: "sub5", 6: "sub6"} }

if a in ["mon","tue","wed","thu","fri","sat"]:                                             # This if else ladder returns which subject period it needs to                                                                                                         
    if current_time >= '9:00:00' or current_time <= '10:00:00':                            # join by checking with realtime
        b = day[a][1]
        link = period [b]
    elif current_time >= '10:10:00' or current_time <= '11:10:00':
        b = day[a][2]
        link = period [b]
    elif current_time >= '11:20:00' or current_time <= '12:20:00':
        b = day[a][3]
        link = period [b]
    elif current_time >= '13:20:00' or current_time <= '14:20:00':
        b = day[a][4]
        link = period [b]
    elif current_time >= '14:30:00' or current_time <= '15:30:00':
        b = day[a][5]
        link = period [b]
    else:
        b = "youtube.com"
        link = period[b]

if b in ["sub1","sub2","sub3"]:                     # edit the greet message according to the subjects 
    greet = "  Good Morning mam !"
elif b in ["sub6","sub5","sub4"]:
    greet = "   Good morning sir!"
    
def OpenMeetLink(a):                                 
    cameraX,cameraY = 766,718                       # change the co-ordinates according to your display ratio and resolution
    micX,micY = 687,718 			                # mic button
    joinX,joinY = 1265,580			                # join button
    chatIconX,chatIconY = 1607,115		            # chat button
    chatboxX,chatboxY = 1714,907		            # chat box area
    sendX,sendY = 1881,904			                # send button

    url = str(link)
    webbrowser.open_new(url)
    sleep(10)
    py.click(cameraX,cameraY)                       # py.click function will use your mouse to click the buttons which are in given coordinates
    py.click(micX,micY)
    py.click(joinX,joinY)
    sleep(10)

    py.click(chatIconX,chatIconY)
    sleep(5)
    py.click(chatboxX,chatboxY)
    py.write(greet, interval = 0.25)
    py.click(sendX,sendY)
    sleep(42000) 
    OpenMeetLink(a)                                 # This is a recursive funnction so that after period ends the code will run gain and joins next class for you 

OpenMeetLink(a)
