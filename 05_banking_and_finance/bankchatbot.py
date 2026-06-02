#CHAT BOT 
import random # for random response
import re # for regular expression

def bot_reponse(text): #create function to get the bot response
    text = text.lower().strip() # convert text to lower case and remove leading/trailing whitespace
    
    
    greet_response = {  #create a dictionary to store regex patterns and corresponding responses for greetings
         r"\b(help|support|assist)\b":[ #use regex to detect keywords related to greetings and support
            "How can I assist you today?", #provide multiple responses for variety
            "What do you need help with?",
            "what do you need support with?",
            "I'm here to help! What can I do for you?"
        ],
         
            r"\b(hello|hi|hey)\b":[ #use regex to detect keywords related to greetings
                "Hello there!",
                "Hi! How can I help you?",
                "Hey! Nice to meet you!"
            ],
            
            r"\b(bye|goodbye|see you)\b":[ #use regex to detect keywords related to farewells
                "Goodbye! Have a great day.",
                "See you later! Take care.",
                "Bye! Hope to talk to you again soon."
            ]
    }
    

    business_response ={ 
        r"\b(balance|money|account|funds)\b":[ #use regex to detect keywords related to balance and account information
            "Your account balance is $5000.",
            "You have $5000 in your account.",
            "Your current funds are $5000."
        ],
        
        r"\b(transfer|send|move)\b":[ #use regex to detect keywords related to money transfer
            "To transfer money, please provide the recipient's account number and the amount.",
            "You can send money by providing the recipient's details and the amount.",
            "Please specify the recipient and the amount to transfer."
        ],
        
        r"\b(payment|pay|bill)\b":[ #use regex to detect keywords related to bill payment
            "To make a payment, please provide the bill details and the amount.",
            "You can pay your bills by providing the necessary information and the amount.",
            "Please specify the bill you want to pay and the amount."
        ]    
    }


    all_responses = {**greet_response, **business_response} #combine both dictionaries into one

    for all, answers in all_responses.items(): #iterate through the combined dictionary, answers is the list of responses (value) for each pattern
        if re.search(all, text): #use regex search to find a match in the user input (using re library we imported)
            return random.choice(answers) #return a random response from the list of answers for the matched pattern
        
    return "I'm sorry, I didn't understand that. Can you please rephrase?" #come back here to this if no patterns matched


def interact():
    print("Bot: Hello! I'm here to assist you. Type 'bye' to exit.") #initial greeting message
    
    while True: #start an infinite loop to keep the conversation going
        user_input = input("user: ") #get user input 
        
        if re.search(r"\bbye\b", user_input.lower()):
            print(" Bot: Goodbye! Have a great day.") #farewell message when user types 'bye'
            break #exit the loop
        
        response = bot_reponse(user_input) #get the bot response based on user input
        print(f"Bot: {response}") #print the bot response in a formatted string
        
interact() #start the interaction with the bot
        