import yfinance as yf

def get_stock_price(): #function to get the current stock price
    while True: # Loop to continuously ask for stock symbols until the user decides to quit
        symbol = input("\nEnter stock symbol (or 'quit' to exit): ").upper() # Prompt the user to enter a stock symbol and convert it to uppercase for consistency
        
        if symbol == 'QUIT': # If the user types 'quit', exit the loop and end the program
            break # Exit the loop if the user wants to quit
            
        try: # Try to fetch the stock price using yfinance
            # Ticker object fetches data from Yahoo Finance
            stock = yf.Ticker(symbol)
            
            # .fast_info is the quickest way to get the latest price
            current_price = stock.fast_info['last_price'] # Get the current stock price from the fast_info dictionary
            
            if current_price is None: # If the price is None, it means the symbol was not found or there was an issue fetching the data
                print(f"No data found for {symbol}. Is it typed correctly?") 
            else: # If the price is successfully retrieved, print it to the user
                print(f"The current price of {symbol} is: ${current_price:.2f}") # Print the current stock price formatted to 2 decimal places
                
        except Exception as e: # Catch any exceptions that occur during the fetching of stock data and print an error message
            print(f"An error occurred: {e}") #
    get_stock_price() # Call the function to start the stock price retrieval process