class cuboid:
    def __init__(self,l,b,h):
        self.l,self.b,self.h=l,b,h
    def lidarea(self):
        return self.l*self.b
    def totalArea(self):
        return 2*(self.l*self.b+self.l*self.h+self.b*self.h)
    def volume(self):
        return self.l*self.b*self.h
c=cuboid(10,5,3)
c1=cuboid(20,10,5)
print(c.lidarea())
print(c.totalArea())    
print(c.volume())
print(c1.lidarea())
print(c1.totalArea())
print(c1.volume())