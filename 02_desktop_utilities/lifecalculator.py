#life expectancy calculator
print("Welcome to the Life Expectancy Calculator!")

current_age = int(input("Enter your current age:"))

age_expectancy = 100

years_left = age_expectancy - current_age

print (f" you have {years_left} years more to live.")

#convert years_left to  days, weeks, months.

days = years_left * 365 

weeks = years_left * 52

months = years_left * 12

print (f" you have {days} days,  {weeks} weeks, and {months} months more to live.")



#ask the user to input their current age with int() function to convert user input to an integer
#give a fixed age expectancy of 100 years
#calculate the years left to live by subtracting current age from age expectancy
#convert the years left to days, weeks, and months
#print the results to the user in a  "f" formatted string
#use 365 days in a year, 52 weeks in a year, and 12 months in a year for the calculations


 
