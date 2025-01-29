"""
Blind Auction
Click "Open Preview" above to see this file rendered with the markdown.

Instructions
The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.

Welcome to the secret auction program. 
What is your name?: Angela
What's your bid?: $123
Are there any other bidders? Type 'yes' or 'no'.
yes
If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid.

The winner is Elon with a bid of $55000000000
Use your knowledge of Python dictionaries and loops to solve this challenge
"""

import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
auction_bidder={}
while True:
	name=input("What is your name?: ")
	bid=int(input("What's your bid?: $"))
	auction_bidder[name]=bid
	choice=input("Are there any other bidders? Type 'yes' or 'no'.\n")
	if choice=="no":
		break
	else:
		clear()
max_bid=0
bidder=""
for key,value in auction_bidder.items():
    if value>max_bid:
        max_bid=value
        bidder=key
print(f"The winner is {bidder} with a bid of ${max_bid}")
    
