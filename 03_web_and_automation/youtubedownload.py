#Youtube Downloads
import yt_dlp #n Mod/Lib for download

def your_download (url): 
    
    instruct_down = { 
        'format': 'best',               #instruction for the format and best 
        'outtmpl': '%(title)s.%(ext)s'  #instruction to change the  tittles
    }
    
    try: #try this block code
         with yt_dlp.YoutubeDL(instruct_down) as ydl: #turn on the download
            ydl.download([url])
            print("Video sucessfully downloaded")
            
    except Exception as error: #if try doesnt work, then  show error
        print(f"Something went wrong :{error} ") 
    
    
url = input("Enter Youtube URL: ")
your_download(url)

