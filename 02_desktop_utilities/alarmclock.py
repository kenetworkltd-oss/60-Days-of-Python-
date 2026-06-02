#Alarm clock
import datetime #import datetime
import time #import time

def alarm_clock(): #start define function
    your_time = input("Enter the time you want to start work ( HH:MM:SS):") #user enter time to set alarm
    print(f"alarm set for {your_time}...") #print f string and the time you set
    while True: #start loop
        time_now = datetime.datetime.now().strftime("%H:%M:%S")#attached current time from import to a variable
        if time_now == your_time: #if current time (time_now) eqaul the time user set
            print("your alarm ⏰is ringing") #print alarm ringing since it the time now
            print(f"it is {time_now} ⏰ time to go to work ! 💼") #second print that follows
            break #loops break here
        time.sleep(1) # the sleep make the alarm repeat after 1 seconds 
        
alarm_clock() #close define funtion