#File Organizer

from pathlib import Path #tools that look into device user folders
import shutil #move files to one another

file_explorer = Path("C:/users/DELL/downloads") #using path object by setting up variable for it

file_set = {  #create a dic-set that that can easily detect & organize ./extentions in files
            
            "Images" :    {".jpg", ".jpeg", ".png", ".gif", ".img", ".svg" },
            "Documents":  {".pdf", ".txt", ".csv", ".docx"  },
            "Audio":      {".mp3", ".wav", ".aac"},
            "Programs":   {".exe", ".msi", ".dmg", ".pkg"},
            "Codes" :     {".py", ".js", ".css", ".html" }        
}

def file_run ():  
    if not file_explorer.exists():
        print("file_explorer does not exist")
        return #come back, stop looking
    
    for file_check in file_explorer.iterdir(): #start loop
        if file_check.is_dir() or file_check.name.startswith('.'): #check if that item a folder or default device files
            continue #skip those items or files above and continue looping others
        
        
        new_folders = "others"
        for folder, extension in file_set.items():
            if file_check.suffix.lower() in extension:
                new_folders = folder
                break #stop look,a match found
            
        target_dir = file_explorer/new_folders
        target_dir.mkdir(exist_ok=True)
            
        location = target_dir/ file_check.name
        if not location.exists():
                shutil.move(str(file_check),str( location))
                print(f"Moved: {file_check.name} -> {new_folders}")
        else:
            print(f"Skipped: {file_check.name} (Duplicate)")
            
file_run()
print("All done! Files are organized.")
            
            
            
            
            
            
            
                
                
                
                
                
        