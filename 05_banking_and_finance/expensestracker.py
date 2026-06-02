#   Expenses Tracker

Expenditure = [   ]

while True:
    print("\n Expenses Tracker")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Exit")
    
    choice = input("Select between (1-3):")
    
    if choice == "1":
        what = input("what did you buy ? :")
        cost = float(input("how much did it cost ? :"))
        #store the data inside dictionary (key:value)
        things = {"name": what,  "amount": cost}
        #add user expenses into the empty list by using dic first to know the key & value
        Expenditure.append(things)
        print("Expenses Saved !")
        
    elif choice == "2":
        print("\n ")
        total = 0 
        
        #loop through the list
        for things in Expenditure:
          print(f"{things['name']} : {things['amount']}")
          total = total + things["amount"]
        print(f" Total: {total}")
        
        
    elif choice == "3":
        print("Expenses Tracker Exited")
        #loop break here
        break
        
        
    else:
        print("Invalid entry, enter between (1-3)")
        
