# count uppercase letter and lower case letter separately from given string

def count_upper_lower(strings):
    upper=0
    lower=0
    for i in strings:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    return upper,lower
print(count_upper_lower("The quick Brow Fox"))