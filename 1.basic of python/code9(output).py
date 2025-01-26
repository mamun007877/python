#print variable value

x=10
print(x)

#print multiple values

x=10
y=20
print(x,y) #by default space separator thake

#print multiple values with sep="ja diye sep korbo"

x=10
y=20
print(x,y,sep=",")

#print is like println of java

x="mamun"
y="MOLLA"
print(x,y,sep="\n")

#end: TO KEEP VALUE CONSEQUTIVE WAY with end="ja diye sep korbo"

print("hello",end=".")
print("Student",end="...")
print("learn python")

#sep and end together

x=10
y=20
z=10
print(x,y,z,end=".",sep=":")
print()

#formating string
x=10
print("value of x is %d"%x)#for one value
y=20
z=30
print("Sum of %d and %d is %d"%(y,z,y+z))#for multiple value

#replacement operator

x=10
y=3.5
z="mamun"

#way-1:

print("hello, {} x= {} y={}". format(z,x,y))

#way-2:

print(f"hello, {z} x={x} y={y}")