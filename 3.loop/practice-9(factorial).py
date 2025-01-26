n=int(input("enter the factorization number: "))
fact=1
for i in range(n, 0,-1):
    fact*=i 
print(f"factorization of {n}={fact}")

#or
m=int(input("enter the factorization: "))
fact1=1
for i in range(1,m+1):
    fact1*=i
print(f"factorization of {m}={fact1}")
