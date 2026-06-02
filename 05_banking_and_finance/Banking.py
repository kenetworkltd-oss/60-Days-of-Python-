# Banking App
import random #Generate unique number

#making the global variable outside all the def func {empty dic to store data}
users_data = { }


 #def func for account creation
def create_acc():
    #newline message for user
    print("/n Create Your Account")
    
    # user create name & pin
    your_name = input("Enter your name :")
    your_pin = int(input("Create your 4 digit pin :"))
    
    #making sure pin is not above 4 digits by using length
    if len(str(your_pin)) != 4 : #if length count not eqaul (!=) 4
        print("your pin digit must be 4 number only!")
        # go back def func beginning
        create_acc()
    # generate random number from rand-integer(randint)
    random_acc = random.randint(10000, 99999) #generate random number between 10000 and 99999 to make sure the acc num is 5 digit only
    acc_start = "45" #all user acc num must start with this prefix to make it more unique and secure, and also to make sure the acc num is 7 digit only (45 + 5 random digit)
    account_number = acc_start + str(random_acc)  #concatentation 
      
    #save user data into dictionary ("key":vale,)
    users_data[account_number] = {
        "name":   your_name,
        "pin":     your_pin,
        "balance":    0,
        "loan":       0
    }
    
    print("Account Created Successfully!")
    print(f"Your Account Number is: {account_number}")
    print("Do NOT forget this number.")
    
    
    # def func for login/sign in, coz it base on another task(user login)
def sign_in(): 
    
     print("/n Welcome, LOGIN ")     
     user_acc = input("Enter your account number: ")
     user_pin = input("Enter your 4 digit pin:  ") 
     
     #check if user acc exist in the dic store
     if user_acc in users_data :
         
         #go to the dic database, look through acc num (the nested " ":) and  match with the key pr label of "pin":
         data_pin = users_data[user_acc]["pin"]
         
         if user_pin == data_pin:
             print("Login Sucessful")
             #if login works, come to the next page which is menu_navigate()
             menu_navigate(user_acc)
                
         else:
             print(" Invalid Pin")
             
     else:
         print ("Account not exist")
         
 #def func for Bank navigation menu (parameter target specific user account_number)
def menu_navigate(account_number):
    while True:
        print("\n Navigate the Banking Menu 1-4")
        print("1.Enter Deposit")
        print("2. Enter Withdrawal ")
        print("3. Check Balance")
        print("4. Exit or log out ")
        
        select = input("select an option between (1-4) :")
        
        
        if select == "1":
            amount = float(input("Enter amount to deposit :"))  #dic var name & dic nested & key & user input(amount)
            users_data[account_number]["balance"] += amount #locate balance and add to user amount
            print(f"${amount} Sucessfully Deposited")
            
            
        elif select == "2":
            amount = float(input("Enter amount to withdrawl :")) #amount to withdraw
            current_bal = users_data[account_number]["balance"] #indictae balance # go to the dic data, look through acc num, and match it with the key or label of "balance":
            
            #to prevent theft or double withdrawl, 
            if current_bal >= amount: #confirm if the  balance greater than or eqaul the amount
                users_data[account_number]["balance"] -= amount #locate balance and subtract from user amount
                print(f"{amount}: successfully withdrawl")
                    
            else:
                print("Error ! Insufficient Balance")
                
            
        elif select == "3":
            figure = users_data[account_number]["balance"]  #go to the dic data, look through acc num, and match it with the key or label of "balance":
            print(f"Your balance is : $ {figure}")  #figure eqaul balance so print figure in f string format
            
            
        elif select == "4":
           print("Banking Menu Exits...")      
           break #loop break 
    
        else:
            print("Invalid options !Enter or select (1-4)")
            
            
# Runing the App (continuation) by just calling out all the def func we've written above

print("/n WELCOME TO SIMPLE BANKING APP")

while True: #start with loop
    print("\n THE MENU ")
    print("1. Create Account ")
    print("2. Sign in")
    print("3. Exit ")
    
    option = input("Enter option : ")
    
    if option == "1":
        create_acc() #calling out the def func only (no need to re-write code)
    
    elif option == "2":
        sign_in()  #calling out the def func only (no need to re-write code)
        
        
    elif option == "3":
        print("Bye for now !")
        break #loop break here
    
    else:
        print("invalid option, try (1-3)")
        