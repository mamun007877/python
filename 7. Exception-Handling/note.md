# What are Exceptions and types of error
- Exceptions are runtime error
#### Syntax error :-
- If there is the typing mistake in the program then it will show syntax error
            
            if x>y
            print(“something”)
- In if statement :(colon) is missing and in print indentation is missing
- This types of errors is said as syntax error. If there is syntax error then the program will not run
#### Logical error :-
    a = 20
    b = 7
    c = 2
    d = a / b-c
    d = 20/7-2 = 4 //0
- How can we correct this logical error . By adding parentheses to it
    
        d = a // (b-c)
- By doing this the answer will be 4


# Programmer user exception
- Developer develops software or app and client uses it
### Types of errors
1. syntax error
2. Logical error
3. Runtime error

#### A developer has to give error free software to user
1. Syntax error: developer is responsible for syntax error.

2. Logical error: These errors depicts flaws in the logic of program The program might be using
wrong formula or the design of the program is wrong itself . Logical errors are not detected either
by python compiler or Pam. The programmer is solely responsible for them.
3. Runtime error: The reason could be giving invalid input File not available, no connection, etc.

    - Runtime errors are caused due to mishandling a software at client side
    - Due to runtime error program crashes stops suddenly
    - User is responsible for runtime error
    - But when developer gives robust idea it can be handled means Exception handling given in program.
#### How to handle the runtime error?
- Example:
    - A printer :
        
            When the manufacturer gives any property on which the printer will blinks if paper is not inserted.It blinks because it needs some input means it is raising an exception.Like wise also a developer can raise an exception asking user to check if there is anything missing.

## Examples of Exception
1. Index error
2. Key error
3. Value error and type error
4. Zero division error

#### When these errors occur
    L=[10, 20, 30, 40, 50]
    index=int(input(‘enter a index’)) # user has to enter value here

    print(L[index])

- If we print valid index it will print else
- If not valid index it will print error
- So ,user itself is responsible for giving wrong index
#### What our program can do ?
- It can give a message”please enter a index which is from 0 to 4 only”
- Now there in output the error will be given as traceback, means it is showing in which line the
error is appearing.
### Index error: 
- List index out of range

### Value Error and Type error:
    val= int(‘abc’) # here we are doing type conversion
    res=‘2’+3 # this type is called as value error
We are saying here (‘2’+3)
2 to be concatenate with 3
But it is a string how can a type int be concatenated with string
        
        a=10
        s=‘number’ THIS IS TYPE ERROR
        print(s+a)
### Key error:
    D=[1:’a’, 2:’b’, 3:’c’]# dictionary list
    key=int(input(‘Enter a key’))//3
    print(D[key])
    
    D={1:’a’, 2:’b’, 3:’c’}
    key= int(input(‘Enter a key’))//6
    print(D[key]) # it will show key error
- Two possibilities of getting an error
    1. Not entering a proper key and
    2. entering string instead of integers
### Zero Division Error:
    a= int(input(‘Enter first number’)
    b=int(input(‘Enter second number’)
    res=a//b
    print(res)# it will show zero division error

# Exception Handling construct
- We will learn how to handle exception in python.
Python skeleton for try-except
- syntax:

        1)———
        2)———
        3)———
        Try:
            4)——-
            5)——-
            6)——-
        Except:
            7)——-
        8)——-
        9)———
        10)——-
    - This may cause Exception . So the lines which may cause Exception are written inside the block.
    - Inside except we may print the message about the exception.
    - The program starts running from the first line then continue 2,3,4,5,6 then it will not go to line 7 as there is no error.
        ### What happens if there is no error?
        - First line , second line gets executed then third fourth . Suppose there is an error in 5t line.The exception raised in 5th line then it will not execute in 6th line.

        - It will directly jump to 7th line I.e except block.

        - If there is any exception in try block then it will execute except block. If condition gets in 4th , 5th and ,6th will not execute and remaining 8910 execute properly.
        
        - The programme executes successfully it will not get terminated or crash abruptly it gets terminated gracefully
        
        - If suppose try and accept has not been used.
        
        - If there is an exception. In the 4th line . The program will crash
            
            
                Program

                l=[10,20,30,40,50] //list of 5 elements

                index=int(input("enter index")) //taking input as index

                print(l[index])
                print("terminated gracefully")
                
                
                Output:
                    enter index3
                    40
                    terminated gracefully
                    
                    enter index9

                    Traceback (most recent call last):
                    File "/Users/abdulbari/PycharmProjects/pythonProject/python programs.py", line 3, in <module>
                    print(L[index])#printing the element at given each given index
                    IndexError: list index out of range
                    If the index is out of range it will get an exception error i.e index error
                    If we give an invalid index it will raise an exception
                
                
                Program 2:

                l=[10,20,30,40,50] //list of 5 elements

                try:
                    index=int(input("enter index")) //taking input as index

                    print(l[index])
                except:
                    print("invalid index")
                print("terminated gracefully")

                
                Output 1:
                    enter index3
                    40
                    terminated gracefully
                
                Output2:
                    enter index9
                    invalid index
                    terminated gracefully
                
                Now the program does not crash it executes safely.