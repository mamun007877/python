n=int(input("enter the series length: "))
a=int(input("enter the 1st term of the series: "))
d=int(input("enter the common difference of the series: "))

for i in range(n):
    print(a+i*d, end=" ")