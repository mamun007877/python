# take positional argument and print message eg. my name is x,i am doctor.

def posArg(name,profession,/):
    print(f"My name is {name}, I am {profession}.")

nam=input("Enter your name: ")
profesion=input("Enter your profession: ")
posArg(name=nam,profession=profesion)