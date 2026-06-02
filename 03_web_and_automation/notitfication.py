# Notification App

import time #import time coz of the time sleep

from plyer import notification #import plyer module/library for notification hardware commands

while True: #start loop
    notification.notify( #bring out (notification.notify) tools that comes with plyer
        title = "work time reminder", #notification title
        message =  "it is time to work", #notification message
        timeout = 5, #from plyer lib, how long the notification display on devices screen
    )
    
    print("notification sent") #message when notication happen
    
    user_entry = input("Enter (START/STOP) to wait for the next reminder or to exit").upper() #user input
    
    if user_entry == "STOP": #if user entry eqaul stop then stop
      print("Notification Stop!") #message when notification discontinues
      break #loops break immediately
  
    elif user_entry == "START": #else if user enter start again
      print("waiting for 20 seconds to start again") #message to print while time sleep
      time.sleep(20) #20 seconds time sleep
      
    else: #if any other input enter
        print("Invalid input, please enter START/STOP to use Notification") #message to print