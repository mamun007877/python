# checking and removing if there is any duplicate in a list

l=[3,5,9,8,3,4,5,9,6,3,7,2]
new_l=[]
for i in l:
    if i not in new_l:
        new_l.append(i)
print(new_l)

