f=lambda a,b:a+b
print(f(2,3))

s=lambda a,b:a if a>b else b
print(s(2,3))

# lambda with filter
l=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x:x%2==0,l)))