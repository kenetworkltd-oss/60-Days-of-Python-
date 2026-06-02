#Password Generator 

import random

print("Welcome to the password generator!")
print("lets create a secure password for you")

generator_character = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@*%$#&")

password_lenght =int(input("how many character do you want in your password?:"))

your_password = "" 

for i in range (password_lenght):
    random_character = random.choice(generator_character)
    
    your_password = random_character + your_password

print(f" your given password is :{your_password}")


    #import the random module to generate random characters
    #create a string variable that contains all the characters you want to include in your password (a,b,c,...,A,B,C,...,0,1,2,...,!@*%$#&#)
    #ask the user to input the lenght of the password they want
    #create an empty string variable to store the generated password
    #use a for loop to iterate over the range of the password lenght
    #inside the loop, use random.choice() function to select a random character from the string variable containing all characters
    #concatenate (add +) the selected random character to the  empty password variable
    #after the loop ends, print the generated password to the user