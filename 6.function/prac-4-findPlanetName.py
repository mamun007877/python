# find a planet name by given id as parameter
'''
id 1: Mercury
id 2: Venus
id 3: Earth
id 4: Mars
id 5: Jupiter
id 6: Saturn
id 7: Uranus    
id 8: Neptune   
id 9: Pluto
'''
import random
def find_planet(id):
    if id==1:
        return "Mercury"
    elif id==2:
        return "Venus"
    elif id==3:
        return "Earth"
    elif id==4:
        return "Mars"
    elif id==5:
        return "Jupiter"
    elif id==6:
        return "Saturn"
    elif id==7:
        return "Uranus"
    elif id==8:
        return "Neptune"
    elif id==9:
        return "Pluto"
    else:
        return "Unknown"
id=random.randint(1,10)
print(f"Planet name is {find_planet(id)}")

# another way to do this
def findPlanet(id):
    planet_dict={1:"Mercury",2:"Venus",3:"Earth",4:"Mars",5:"Jupiter",6:"Saturn",7:"Uranus",8:"Neptune",9:"Pluto"}
    return planet_dict[id] if id in planet_dict else "Unknown"
id=random.randint(1,10)
print(f"Planet name is {findPlanet(id)}")