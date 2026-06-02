# Guessing Game

import random

guess_number = random.randint (10, 20)

# hack the answer by using Print the number via the varaible, guess_number
#print(f" The answer is :{guess_number}")


print("welcome to the guessing game!")
print("I am thinking of a number between 10 and 20.")


user_guess = int(input("Enter your guess:"))

if guess_number == user_guess:
     print("Congratulations! you won the game")

    
elif guess_number > user_guess:
        print("Too low! try a higher number")
    
else: 
  print("Too high! try a lower number")
    
    #create a guessing game where the user has to guess a number between 10 and 20
    #import the random module to generate random numbers
    #use randint function to generate a random number between 10 and 20 , 'randint' means random integer
    #ask the user to guess the number
    #use if statement to check if the user guess is equal to the generated number
    #use elif statement to check if the user guess is greater than the generated number
    #use else statement to check if the user guess is less than the generated number