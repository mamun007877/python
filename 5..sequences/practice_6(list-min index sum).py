# minimum index sum of two list
fav1=['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta','burger']
fav2=['burger','hotdog','noodles','pasta','nuggets','pizza']

min_sum=float('inf')
for i in fav1:
    if i in fav2:
        if min_sum>fav1.index(i)+fav2.index(i):
            min_sum=fav1.index(i)+fav2.index(i)
print(min_sum)