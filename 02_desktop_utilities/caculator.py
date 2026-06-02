#Simplecalculator

step1 = float (input ("Enter your first number:"))

calculation_symbol = input (("Enter an operation (+, -, *, /, //, %):"))

step2 = float (input ("Enter your second number:"))


if calculation_symbol  == "+":
    print(f"answer:{step1 + step2}")
    
elif calculation_symbol == "-":
    print (f"answer:{step1 - step2}")
    
elif calculation_symbol == "*":
    print (f"answer:{step1 * step2}" )
    
elif calculation_symbol == "/":
    print (f"answer:{step1 / step2}" )

elif calculation_symbol == "//":
    print (f"answer:{step1 // step2} ")
    
elif calculation_symbol == "%":
    print (f" answer:{step1 % step2 }")
    
else :
    print ("invalid calculation")


#ask the user for two numbers
#using float to allow decimal inputs (0.0)  
#ask the user which calculation symbols to use 
#print based on the symbol & input provided by the user
#using if statements "is it this?"
#using elif statements "is it this other thing?"    
#using else statement "if nothing matches then print this "invalid calculation"