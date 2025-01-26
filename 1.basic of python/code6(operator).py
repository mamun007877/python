#arithmetic operator
print(3**2)#exponent
print(10**-2)#exponent
print(13/5)#divide(float)
print(11//5)#divide(floor)
print(10*5)#multiply
print(11%5)#reminder
print(10+5)#addition
print(10-5)#substraction
print("10"+"5")#concatination
print("10"*5)#reptition
print("-------------------")
#relational operators

print(3>5)
print(3<5)
print(5>=4)
print(5<=6)
print(5==6)
print(5!=6)
print(4+4j ==4+4j)
print("-------------------")

#logical operators

print(5>6 or 5<6)
print(5>4 and 4<5)
print(not 5>6)
print(5>6 and 5<6)
print(5<4 or 6<5)
print(not 7>6)

print("-------------------")

#bitwise operator

print(5&6)
print(5|6)
print(5^6)
print(~5)
print(25>>2)
print(12<<3)
print("-------------------")
#assignment operator
x=100
x+=5
print(x)
x-=5
print(x)
x*=5
print(x)
x/=10
print(x)
x//=5
print(x)
x%=2
print(x)
x**=3
print(x)
x=100
x&=2
print(x)
x=100
x|=2
print(x)
x=100
x^=2
print(x)
x>>=2
print(x)
x<<=3
print(x)
print("-------------------")
#identity operator

m=5
n=5
print(m==n,m is n)
m=10
n=10.0
print(m==n,m is n)
print("-------------------")
#membership operator
x="abc"
print("a" in x)
print("A" in x)
print("a" not in x)
print('A' not in x)
print("-------------------")

l,b,h,a=5,4,5,4
rec_area=l*b
tri_area=.5*b*h
rom_area=(a+b)*h/2
v,u,a=50,0,2.5
displacement=(v**2-u**2)/(2*a)
equal_roots=-b/(2*a)

print(f"rec area {rec_area}\ntri area {tri_area}\nthe area_rom {rom_area}\ndispalcement {displacement}\nequal roots {equal_roots}")