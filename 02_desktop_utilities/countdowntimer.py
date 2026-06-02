#Countdown Timer for my birthday

import datetime
import time

birthday_date = datetime.datetime(2027,1,23, 0,0,0)
print(f"Counting down to {birthday_date}")

while True:
    today_date = datetime.datetime.now()
    time_left = birthday_date - today_date
    
    if time_left.total_seconds() <= 0:
       print("Happy birthday")
       break
    print(f"time left :{time_left}", end ="\r")

    time.sleep(2)