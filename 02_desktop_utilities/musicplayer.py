#MUSIC PLAYER 

import pygame #import sys
import time #import time module to add delay in the music player
import os # Initialize the mixer module

def music_player(file_explorer): #function to play music
    pygame.mixer.init() # Initialize the mixer module
    pygame.mixer.music.load(file_explorer) # Load the music file
    
    pygame.mixer.music.play() # Play the music file
    print(f"playing music {file_explorer}") #print the name of the music file being played
    
    while pygame.mixer.music.get_busy(): # Check if the music is still playing
        time.sleep(3) # Add a delay to prevent the program from exiting immediately after playing the music
   
file_explorer = input("Enter which of the music : ") # Prompt the user to enter the name of the music file they want to play

if os.path.isfile(file_explorer): # Check if the file exists before trying to play it
    music_player(file_explorer) # Call the music player function with the provided file name
    
else: # If the file does not exist, print an error message
    print("file not found, please check the file name and try again") # Print an error message if the file is not found
