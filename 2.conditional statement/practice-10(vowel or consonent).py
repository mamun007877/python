# check if given lower case character is a vowel or conson
character=input("Please enter a character:")

# convert character to lower case
if 97<=ord(character)<=122:
    if character=="a" or character=="e" or character=="i" or character=="o" or character=="u":
        print(f"{character} is a vowel.")
    else:
        print(f"{character} is a consonant.")
else:
    character=chr(ord(character)+32)
    if character=="a" or character=="e" or character=="i" or character=="o" or character=="u":
        print(f"{character} is a vowel.")
    else:
        print(f"{character} is a consonant.")