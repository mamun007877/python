# check if maximum difference between 2 numbers is less than 5
def diffNum(num1,num2):
    if abs(num1-num2) < 5:
        return True
    return False

print(diffNum(10,5))
print(diffNum(10,6))