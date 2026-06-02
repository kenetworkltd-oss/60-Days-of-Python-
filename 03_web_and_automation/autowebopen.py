#AUTO WEB OPEN AND TARGETED PAGE FROM USER 

import webbrowser #to open default browser and get info from it

Page = input("where would you like to search on goggle :").strip() #collect user info to know the exact page to open 

url = "https://www.google.com/search?q="  #the main web link to first open

target = url + Page  #add both user page and url link together

print(f" opening the {target} on google:") #in f string message to show while opening

webbrowser.open(target) #the tools to make the main final link needed to open
