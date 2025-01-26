# #transpose matrix

l1=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l=[]
for i in range(len(l1[0])):
    l2=[]
    for j in range(len(l1)):
        l2.append(l1[j][i])
    l.append(l2)
print(l)