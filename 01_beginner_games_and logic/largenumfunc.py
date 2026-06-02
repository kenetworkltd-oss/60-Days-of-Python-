def num_big():
    
    taker_1 = int(input(" Enter first number: "))
    taker_2 = int(input("Enter second number:"))
    
    while True :
        if taker_1 > taker_2:
            print(f"{taker_1} is the larger number")
            break
    
        
        elif taker_2 > taker_1 :
            print (f"{taker_2} is the larger number")
            break
            
        elif taker_1 == taker_2 :
            print ("no number is larger")
            break
            
        else:
            print("invalid input")
            
num_big()