#Dice Rolling Game

import random #import random module

def play_dice(): #make a definen function to keep the game inside
    print("Welcome to rolling the Dice") #first welcome print for the user
    result = random.randint (5, 10) #give a random integer between 5-10
    print(f"You have rolled:{result}") #the computer show what number it picks
    
while True: #loop start
    player = input("Do you want to roll the dice ? (yes or no)").lower() #select yes or no start the game
    if player == "yes": #if user select yes
        play_dice() #game start and the def function come here and show what number the computer picked 
    elif player == "no": #if user select no
        print("Thanks for playing, Goodbye!") #show this to user
        break #loop break here
    else: #if user select anything other than (yes or no)
        print("wrong entry, please type (yes or no) to start the game") #show this to user
