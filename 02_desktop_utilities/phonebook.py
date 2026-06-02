#Phone Book

def phonecontact_app():
    
    phone_contact = {}
    print("welcome to Phone Contact")
    
    while True:
        print("\n Phone Book Menu")
        print("1. Add Contact ")
        print("2. View list of Contact ")
        print("3. Search Contact")
        print("4. Delete Contact ")
        print("5. Exit Contact")
        
        User_select = input("Select option between (1-5) :")
        
        if User_select == "1":
            create_name = input("Enter contact name:")
            create_num = input("Enter the number:")
            phone_contact [create_name] = create_num
            print (f"New Contact of {create_name}  added succesfully")
            
        elif User_select == "2":
            if len(phone_contact) == 0:
                 print("phone contact is empty")          
            else:
                print("\n Contact list")
                print(f"{phone_contact} ")
                
        elif User_select == "3":
            user_search = input("Enter contact to search:").title()
            result = phone_contact.get(user_search)
            if result:
                print(f"Found!{user_search}:{result} ")
            else :
                print(f"{user_search} not found")
                
        elif User_select == "4":
            user_search = input("Enter contact to delete:")
            result = phone_contact.pop(user_search, None)
            if result:
                print(f"{user_search} has been deleted sucessfully!")
            else :
                print(f"{user_search} not found")
                
        elif User_select == "5":
            print("Goodbye!")
            break
        
        else:
            print("Option not found, try enter between (1-5)")
        
phonecontact_app()
        