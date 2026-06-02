#Chat Bot

import re #use import of regex (regular expression)

def get_result(text): #create function  parameter to use later``
    
    text = text.lower() #indicate lower case
    
    Mochi = { #create dictonary to store bot replies and text to detect
             "name": "My name is Mochi, i am here to help you",
             "how are you?": "i'm good, how can i help you ?",
             "hello": "Whats on your mind",
             "hi": "Hi there, how can i help you today",
             "date": "Today is saturda~y",
             "bye": "Goodbye! Have a great day.",
    }
    
    for keyword, response in Mochi.items(): #check if any keyword exist in text def func
        if keyword in text: #and if it exist
            return response #return response
        
    return "i don't understand, can you rephrase better?" #return this
    
    
    
def chat():  #second def function
        print("mochi: Hello type bye to exist.") #first print under def func
        
        while True: #while loop start
            
            text = input ("User: ") #get user input
                
            if text.lower() == "bye": #find the exit condition to break the while
                print("Mochi:Goodbye! Have a great day") #print  this incase user try to exit
                break # while loop break
            
            result = get_result(text) #to print the result from the first def  and dictionary we created i begin #response or result from the key in dic we created above
            print(f"Mochi:{result} ") #michi response and the result in f string
            
chat() #run the second def func