# Tuple Intro
## Tuple DataType
- This is one more datatype in python it is similar to list . 
- The only difference is tuple is immutable and list is mutable .means it is only readable.
- Tuple is collection of elements
    
        Ex: tuple 1=(‘jack’, 45,38.6,false, 5+6j, ‘Jill’, 45)
- Tuple can contain duplicates also.
# How to create Tuple
- Tuple is enclosed in round brackets
# How it looks in memory?
- It looks like an array. So this is an array and every array having its own index
- We cannot change anything in tuple tuple does not has append method so, we cannot change the value at a particular and nor increase it.

        1. t1=(1,2,3,4,5) #this is the method of  creating a tuple
        2. t1=(10)#single value in a tuple# not valid
        3. t1=(10, ) # valid //t1=(10)
        4. t1=tuple((1,2,3,4,5)) //t1= (1,2,3,4,5)
        5. t1=()
        6. t1=tuple([1,2,3,4]) //t1=(1,2,3,4)
        7. t1=tuple("pythons") //t1=("p","y","t","h","o","n")

        so using tuple(itearable) we can create tuple
# Packing:
    1. t1=10,20, 30,40 #giving multiple values what happens ?Let’s check.
    t1=10
    t1
    10
    type(t1)
    <class 'int'>

    2. t1=10,20,30,40 # it is called packing
    type(t1)
    <class ‘tuple'>
- If we give multiple values it will pack it by giving brackets this is called packing
# Unpacking:
    t2=(10,20,30,40)
    a,b,c,d=t2
    t2=(10, 20, 30, 40)
    a=10
    b=20
    c=30
    d=40
- This is called unpacking
- When given values without parenthesis means packing and in contrast given values which are storing them is called unpacking are automatically used in tuple

        t1=10,20,30,40
        l1=[1,2,3]
        type(l1)
        <class 'list'>
        a,b,c=l1
        a
        1
        b
        2
        c
        3
- Unpacking is done for tuple as well as list and string. But packing happens only with tuple


# Tuple comprehensions and methods
## Comprehension
- comprehensions are short cut for creating a sequence object or tuple object.
Let’s Try:

              1. t=tuple(i for i in range(int))

              2. t=(*(i for i in range(int)),)  

              3. t=(*(i for i in itarable),)

- Now creating another tuple

        1. t= (*(x for x in string if x.islower),)
        2. t= tuple((x for x in string if x.islower))
- method
        
        most of list method work here accept add and remove methods

        1. var.count(value)

        2. var..index(value)    //Index method gives an error when the element is not found

        
# Tuple Iteration and Operators
## Iteration
- traversing and visiting all the elements of a tuple .
                
        t1=(‘jack’, 45, 38.6, false, 5+6j,’Jill’, 45)#this is a tuple

- Iteration can be done using for loop

        t=(1,2,3,4)

        1. for i in t:
                print(i)
        2. for i in range(len(t)):
                print(t[i])
        
        This can be done using while loop also
## Operators in tuple

- Index []
- Slicing [:]
- Concatenation +
- Repeat *
- Membership in/not in

- all work like list

