"""
Write a program for a reverse park to handle reservations and fees management.
Fee catergory: Adult = 2,500; Teenage (between 9 - 17) = 1,200; Children < 8 = 0.
Note: for a group above number of 8, there will be a discount of 20% on total fee.  
If coming in with media device such as a camera, extra charge( of 1000) should be added.
Solution Breakdown 
  1. How many people/individuals 
  2. catergory - Number of adults, teens, Children
  3. With media device ?
  4. Price cost/fee
"""

#Reverse park fees management system

adult_group = int(input ("How many adults are in your group ?"))

teenage_group = int(input ("How many teenagers are in your group (between 9-17) ?"))

children_group =int(input ("How many children are in your group (under 8) ?"))

with_camera = input ("are you coming with a camera or media device ? (yes/no)").lower()

adult_total = adult_group * 2500
teenage_total = teenage_group * 1200  
children_total = children_group * 0

total_fees = adult_total + teenage_total + children_total

total_group = adult_group + teenage_group + children_group 

if total_group > 8:
    print ("You are eligible for a 20% discount on total fees")
    discount = total_fees * 0.20
    total_fees = total_fees - discount
    
if with_camera == "yes":
    total_fees = total_fees + 1000

print (f"Your total park fees to pay is ₦:{total_fees:.2f}")


#ask the user for number of adults, teenagers, children in the group
#ask the user if they are coming with a media device such as camera
#calculate the total fees based on the catergory rates
#apply a 20% discount if the group is more than 8 individuals
#add an extra charge of 1000 if coming with a media device
#display the total fees to the user in a formatted string with 2 decimal places (:.2f)
