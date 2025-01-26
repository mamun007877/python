# pascal triangle
def pascal_triangle(n): 
    r=[1]
    for i in range(n+1):
        print(" "*(n-i),end=" ")
        for j in r:
            
            print(j,end=" ")
        print()
        #print(r)
        tr=[0]+r
        r=r+[0]
        nr=[x+y for x,y in zip(tr,r)]

        r=nr
pascal_triangle(5)
