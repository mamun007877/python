# concatenate all int from a list to a single number
l=[3,5,10,7,12]
s=''
for i in l:
    s+=str(i)
print(int(s))