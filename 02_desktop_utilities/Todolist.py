 #To do list program 

def main(): #start with define function
      
    task = [  ]  #create empty list 
    
    print("Welcome to do list app") #first print to welcome user 
    
    
    while True: #start loop
        print ("\n Option:")     #print list of option for user to select   
        print ("1. Create a task ")
        print ("2. Open a task")     
        print ("3. Delete a task")
        print ("4. Exit ")
        
        select = input("select your option (1-4) :") #ask user to input option between 1-4
        
        if select == "1": #if user select equal 1
            
            title = input ("Create a new task title:") #then ask user for task title
            
            details = input ("Enter task description :") # then ask user for task full details
            
            full_task = (f"{title}:{details}") # then combine them nicely
            task.append(full_task)     #use .append() to join the user task to the list
            print (f"Task {full_task} Added!:") #print those entry has been added formatted string
            
        elif select == "2": #if user select 2 and
            if len (task) == 0:  #the len eqaul 0 
                print("your task is empty") #display task is empty
            else:
                print ("\n your tasks") #otherwise show list of task
                for i in range(len (task)): #loop inside the task
                     print(f"{i + 1}. {task[i]}") #add more incase of edit in task file
                 
                    
                    
        elif select == "3": #if user select 3
            if len (task) == 0:  #and the lenght inside is eqaul zero which means nothing inside
                print("No task to delete")   #show nothing inside
            else: #otherwise
                task_num = int(input("Enter task number to delete:")) #enter the number to delete
                delete_task = task.pop(task_num - 1) #the selected number will pop which indicate delete
                print(f"deleted: {delete_task}") #task or file deleted
                
        elif select == "4": #if user select and it equal 4
            print("Goodbye!") #show goodbye
            break #loop stop or break here
        else: 
            print("Option not found. please try again") 
            #if user select any other number aside the ones listed above, show option not found
main() #call out
