# Introduction to Dictionary
- Dictionary is a collection of key - value pair
- It works similar to real life dictionary which contains word and their meaning
- Searching is done based on dictionary Keys
- Dictionary is created as

        dict = { ‘fruit’ : ‘apple’, ‘vegetable ’ : ‘carrot’ , ‘dish’ : ‘salad’}

        fruit , vegetable and dish - keys
        apple , carrot and salad - values
- For values you can take any Datatype
- But for Keys you can take only immutable Datatype( i.e ,excluding set and listdatatype )
- We can perform the following on Dictionary I.e; Access , Insert , Update and Delete

        dict={101:'john',102:'mark',103:'david'}

## Access
- For accessing any value use key inside [ ]
        
        # accessing by dict[key]

        1. dict[101] //mark
        2. dict[0] // No key with 0 value so we got error
## Update
- It updates the existing value in a dictionary using respectable key
        
        # Updating dictionary by dict[key]=value
        dict[103]='smith' //103:'smith'
## Insert
- New keys and pair are inserted using insert in a dictionary
        
        #inserting in dictionary by dict[key]=value
        dict[104]:'mamun' //104:'mamun'
## del
- To delete a particular value write del keyword , dict name then key inside [ ]
        
        # deleting an item using keyAccess by del dict[key]

        del dict[104]
- You can also delete the complete dictionary using del keyword

        del dict
## Traversing
- You can use for loop for traversing through a dictionary then you'll get keys as output

        for i in dict:
            print(i)    // only keys as output
            
        - Suppose you want to print both key value using for then do this

        for i in dict:
            print(i,dict[i]) //Key - value as output

# Dictionary Comprehensions
1. dict1 = dict( )
    - Its an empty dictionary
2. dict5 = { }
    - Its an empty dictionary
3. dict2 = dict ((iterable pairs))
    
        dict2 = dict(((1,2),(2,4),(3,6)))

        - This are the couple of two elements. This will all form of the dictionary
        {1:2,2:4,3:6}
4. dict3=dict(zip(iterable , iterable))
    - If you have two iterable’s ( it can be list, tuple or string)
    - You can join two iterable so for this zip is used
        
            l1={‘A’,’B’,’C’}
            l2=[‘apple’,’ball’,’cat’]
            d=dict(zip(L1,L2)) //d=dict((('A','apple'),('B','ball'),('C','cat')))
            d={‘A’:’apple’,’B’:’ball’,’C’:’cat’}
    - If the iterable is having extra value then it will be ignored


5. dict4=dict(enumerate (iterable))
    - It will give indexes to the elements but in dict
            
            dict4=dict(enumerate (l1))
    - It will take key and value
6. dict6={exp:exp for item in iterable}
7. dict7={(exp,exp) for item in iterable}
    - Both are same but in dict7 it will act as a tuple
8. dict8={x:y for x,y in zip(iterable,iterable)}
    - It is same as dict3 but in this we use for loop
9. dict9={item for item in enumerate(iterable)}
    - It is same as dict4 but we use for in this