'''
quadratic equation is ax2+bx+c=0

where roots are 

r1=(-b+sqrt(b2-4ac))/2a
r2=(-b-sqrt(b2-4ac))/2a

find the roots of quadratic equation

'''
import math
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=int(input("enter the value of c: "))
r1=(-b+math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
r2=(-b-math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
print(f"the two roots r1 = {r1} and r2 = {r2}")