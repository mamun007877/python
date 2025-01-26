# digit count and sum of digits and reverse digit and check palindrome
number=int(input("enter the number: "))
count_digit=0
n=number
sum=0
stre=""
while number>0:
    sum+=number%10
    stre+=str(number%10)
    number=number//10
    count_digit+=1
    
print(count_digit)
print(sum)
print(stre)
for i in range(count_digit):
    print(int(stre[i]),end="")
print()

if int(stre)==n:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

#anothr way
number=int(input("enter the number: "))
count_digit=0
n=number
sum=0
rev=0
while number>0:
    sum+=number%10
    rev=rev*10+(number%10)
    number=number//10
    count_digit+=1
    
print(count_digit)
print(sum)
print(rev)
if rev==n:
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")
