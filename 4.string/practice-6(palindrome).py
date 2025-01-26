'''
1. checking a string is a palindrome
2. converting a string to palindrome
'''

#1
string_1=input("Please enter: ")
if string_1==string_1[-1::-1]:
    print(f"{string_1} is a palindrome")
else:
    print(f"{string_1} is not a palindrome")

#2
string_2=input("Please enter: ")
if string_2!=string_2[-1::-1]:
    new_string=string_2+string_2[-1::-1]
    if new_string==new_string[-1::-1]:
        print(f"{new_string} is a palindrome")
    else:
        print(f"{new_string} is not a palindrome")
else:
    print(f"{string_2} is a palindrome")