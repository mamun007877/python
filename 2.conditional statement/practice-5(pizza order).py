'''
Pizza Order

Instructions
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1

Example Input
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"

Example Output
Your final bill is: $28.

Hint
Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.
'''
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill=0
if size=="S" or size=="M" or size=="L":
    if size=="S":
        bill=15
    elif size=="L":
        bill=25
    elif size=="M":
        bill=20
    if add_pepperoni=="Y":
        if size=="S":
            bill+=2
        else:
            bill+=3
    if extra_cheese=="Y":
        bill+=1
    print(f"Your final bill is: ${bill}.")
    
else:
    print("Invalid size")