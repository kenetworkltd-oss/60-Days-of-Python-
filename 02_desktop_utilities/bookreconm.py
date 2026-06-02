#BOOK RECONMENDATION SYSTEM
#This is a book recommendation system that recommends books based on the user's preferred genre. The user can select a genre from the list and the system will recommend a book from that genre.

import requests #importing the requests module to make API calls

def book_request(genre): #function to make API call and get book recommendations based on genre
    
    url = f"https://openlibrary.org/subjects/{genre.lower()}.json" #API endpoint to get books based on genre, the genre is converted to lowercase to match the API requirements
    
    response = requests.get(url) #making a GET request to the API endpoint and storing the response in a variable
    
    data = response.json() #converting the response to JSON format and storing it in a variable
    
    list_books = [  ] #creating an empty list to store the recommended books
    
    for works in data[ "works"] [:5]: #looping through the first 5 works in the data and extracting the title and author of each book, then appending it to the list of recommended books
        title = works["title"] #extracting the title of the book from the data
        author = works ["authors"] [0] ["name"] #extracting the name of the author from the data
        list_books.append(f"{title} by {author}")
        
    return list_books #returning the list of recommended books


while True: #starting an infinite loop to allow the user to get book recommendations until they choose to quit
    genre = input("Enter a genre or (quit) :") #prompting the user to enter a genre or quit the program, the input is stored in a variable called genre
    
    if genre == "quit": #if the user enters "quit", the program will print a goodbye message and break the loop to end the program
        print("Goodbye!") #printing a goodbye message to the user
        break #breaking the loop to end the program
    
    print (f"searching for {genre}....") #printing a message to indicate that the program is searching for books in the specified genre
    
    try: #using a try-except block to handle any potential errors that may occur during the API call or data processing
        your_books = book_request(genre) #calling the book_request function with the user's input genre and storing the recommended books in a variable called your_books
        for your_book in your_books: #looping through the list of recommended books and printing each book recommendation to the user
            print(f"Recommended book: {your_book}") #printing each recommended book to the user in a formatted string
            
    except: #if any error occurs during the API call or data processing, the program will print an error message to the user
        print("sorry, error occured, please try again") #printing an error message to the user if an exception occurs during the API call or data processing

    



        
    
    

    