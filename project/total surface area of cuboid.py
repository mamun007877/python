# total surface area of cuboid. it has 6 sides.
'''
front and back= 2(*length*height)
bottom and top=2*(lenght*breadth)
left and right=2*(breadth*height)
total area=2*(lh+lb+bh)
'''

l=int(input("enter the value of length =  "))
b=int(input("enter the value of breadth = "))
h=int(input("enter the value of height = "))

area_surface_of_cuboid=2*(l*b+l*h+b*h)
print(f"surface area of cuboid is {area_surface_of_cuboid}")