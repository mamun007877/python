'''
find sum of numbers ending with 0 from a given list
'''

def sumNum(listNumbers):
    sum=0
    for num in listNumbers:
        if num%10==0:
            sum+=num
    return sum

print(sumNum([100,456,300,200,234,678]))

# another way to do this

def sumNum1(listNumbers):
    sum=0
    for num in listNumbers:
        if str(num).endswith("0"):
            sum+=num
    return sum

print(sumNum1([100,456,300,200,234,678]))