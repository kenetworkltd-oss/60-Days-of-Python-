# currency converter

import requests #coz we are using the API request

api_key = "5d6288df1bee614f6a9ff17e" #api key into variable

print("Welcome to the currency converter")

while True :
    
    from_which_currency = input ("Enter your currency (NGN, USD,EUR,GBP,YEN,CHF):").upper()
    #user enter what currency they have
    
    enter_amount = float(input("Enter amount to convert :")) #user enter amount
    
    to_which_currency = input ("Enter the foreign currency (NGN, USD,EUR,GBP,YEN,CHF):").upper() #what currency they want to change
    
    request_link = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_which_currency}/{to_which_currency}" #api request links
    
    data = requests.get(request_link).json() #json data scraps
    
    rate = data["conversion_rate"] #the variable data [live rate] which json & api fetched
    
    result = enter_amount * rate #  user entry amount multiply by live rate
    
    print (f" {enter_amount} {from_which_currency} rate is {result:,.2f} {to_which_currency}") #display conversion final result
    
    again = input("Do you want to convert another currency,enter(yes/no)").lower() #user enter with lower case to continue or exit
    
    if again.lower() == "no" : #no command
        print("GoodBye! Thank you for using conversion rate")
        break #loop break here