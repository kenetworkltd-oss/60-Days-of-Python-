#Weather App
import requests #import request coz of the API

def the_weather(): #call out define function to start
    
    api_key = "ad6528749866e6f04e1feadcfe53ec53" #API key
    
    base_url = "http://api.openweathermap.org/data/2.5/weather" #api weather, their base website/URL
    
    user_city = input("Enter city to check the weather:") #user enter city to check weather
    
    request_link = f"{base_url}?appid={api_key}&q={user_city}&units=metric" #api request link embeding variable inside
    
    answer = requests.get(request_link) #request library we import to get data from the API
    
    if answer.status_code == 200: #if request is 200 which means sucessful/reachable
        
       data = answer.json() #json data scrap to fetched list of key data & result
       
       weather = data['weather'][0]['description'] #data of weather via (API, Json Data)
       temperature = data['main']['temp']  #data of temprature via (API, Json Data)
       humidity = data['main']['humidity']  #data of humidity via (API, Json Data)
       
       print ("SUCCESS !") #display sucess as starting message for the user
       print(f"Weather in {user_city.capitalize()} ") #user city name begin with capital letter
       print(f"Description:{weather}") #result of weather in f string
       print(f"Temprature:{temperature}°C") #result of temprature in f string
       print(f"Humidity:{humidity}%") #result of humidity in f string
       
    elif answer.status_code == 404: ##if request is 404 means unsucessful/unreachable
         print("city not found, check spellings or enter another city") #message to print if user enter incorrect city spellling or city not found
         
    else:
        print(" Invalid Input") #else for wrong/invalid entry
        
while True: #loop start here
    the_weather() #loop through the whole func we created above
    use_again = input("Do you want to use weather again (yes/no):").lower() #user enter yes or no in small letter wether to continue again or not
    if use_again.lower() == "no": #if user input eqaul no
       print("Weather exited,Bye for now!") #message to display when user enter no
       break #loop breaks

    
    