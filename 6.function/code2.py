#functions with more than 1 input/parameter

def greet_with(name,location):
    print(f"hello {name}")
    print(f"what is it like in {location}?")
#positional argument
greet_with("Mamun","konabari")

#keyword argument
greet_with(location="konabari",name="Mamun")
