#find the most occurrence in the list

count=0
l=['b','b','c','d','e','a','b','c','a','b','b']
l1=[]

l2=[]
for i in l:
    if i not in l1:
        l1.append(i)
        l2.append((i,l.count(i)))   

        
most=0
most_occurrence=None
for i in l2:
    if i[1]>most:
        most=i[1]
        most_occurrence=i[0]
print(most_occurrence,most)
        