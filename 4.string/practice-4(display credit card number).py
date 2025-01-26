'''
display credit card number
card_number: 4554 3663 2595 1142
display:**** **** **** 1142
'''
card_no=input("enter card number: ")
last_4digit=card_no[-4::]
print(last_4digit)
star="*"*4+" "
display=star*3+last_4digit
print(display)
