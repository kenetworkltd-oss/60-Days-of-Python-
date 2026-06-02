#Guess Word
import random #import random modlue to randmoly guess

word_color = ["blue","yellow","green", "purple","orange","pink","red"] #create a list of word to guess with comma,

secret_color = random.choice(word_color)#use random.choice to randomly select one out of the list we created
print("I will guess a color name out of this list:(blue,yellow,green,purple,red)") #give user hints
print("Guess the color") #display what user will do
#print(secret_color)

while True: #start loop
    
    User_guess = input("Enter the color i guess:") #user enter their guess
    
    if User_guess.lower() == secret_color: #if user guess equal the random.choice(secret_color)
        print("You won the game!") #message to show if user win
        print(f"the guess is {secret_color}") #answer show too if win
        break #break loop
           
    elif User_guess != secret_color: #if user guess not matched the random.choice(secret_color)
        print("You lost the Game, try again") #message to show if user lost the game
