# overlaping elements of two list
l1=[10,15,6,9,12,8,4]
l2=[14,6,19,4,7,10,11]
l=[]
for i in l1:
    if i in l2:
        l.append(i)
print(l)