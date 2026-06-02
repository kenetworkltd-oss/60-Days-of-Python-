#Image downloader

import requests  # Using requests to talk to the internet

def img_downloader(url, file_hold): # Create function to reuse later
    try: 
        # We use stream=True to download in small bits
        response = requests.get(url, stream=True) 
        response.raise_for_status()  # Check if the link is valid
        
        # Open the file in 'Write Binary' mode
        with open(file_hold, "wb") as the_file:
            for data in response.iter_content(1024):
                the_file.write(data)
        
        print(f"Great! Image saved as {file_hold}")
                
    except Exception as e:
        # 'e' catches the specific error message
        print(f"An error occurred: {e}")

# The Action (The Trigger)
img_downloader("https://www.python.org/static/img/python-logo.png", "python_logo.png")















img_downloader("https://www.python.org/static/img/python-logo.png", "cool_picture.png")