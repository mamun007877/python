# find maximum of 3 numbers
def maxNum(num1,num2, num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

num1=int(input("enter a number 1: "))
num2=int(input("enter a number 2: "))   
num3=int(input("enter a number 3: "))
print(f"maximum number is {maxNum(num1,num2,num3)}")