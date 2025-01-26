# for loop

->>iterate statements for number of elements in a sequence. number of iteration is knows in advance

- syntex-1:

        for item in list_of_items:
            do something to each item

        example:

        fruites=["apple","peach","pear"]
        for fruit in fruites:
            print(fruit)

- syntex-2:
        
        for i in range(start,end,step):
            do something

- Range function:

    - if we don't use start and step then by default it use 0 and 1 respectively but we must to need to put end value.

    - end value exluded but start value included

    - we can only int value to set start,end and step
    
            example:
            for number in range(1,10):
                print(number)

# while loop

->>iterate statements till some condition is true

    syntex-1: infinite loop unless break use


        while something_is_true:
            Do something
    
    syntex-2:

        initialization

        while condition:
            do something

            increment/decrement
        
        such as

            i=0
            while i<10:
                print(i)
                i+=1

# difference between while and for

->> for is basically use for sequence item like string,tuple,list,dictionary,set,range. it gives each element of sequence item

->>while is basically use for non-sequence number


# transfer statement:

- break,continue,pass

    1. break is use for leave loop to end loop

            chanc=1
            while chance<=3:
                x=int(input("enter an even number: "))
                if x%2==0:
                    break
                chance+=1
                if chance==4:
                    print("you lost")
                else:
                    print("you win")
    
    2. with the continue statement we can stop the current iteraton, and continue with the next 

            x=1
            while x<=24:
                if x%5==0:
                    x+=1
                    continue
                print(x)
                x+=1  

    3. we use pass statement to create empty block

            x=0
            if x==0:
                pass
            print("hello") 


# use of else with loop

- while-else:

        while condition:
            do this
        else:(while er condition false hole else cholbe and jodi loop  break er jnno end hoy tkhn else a dhukbe na)
            do this
        
        example:
        i=1
        while i <=3 :
            x=int(input())
            if x%2==0:
                print("you win")
                break
            i+=1
        else:
            print("you lost")
    
- for-else:

        for i in sequence:
            do this
        else:(jodi loop  break er jnno end hoy tkhn else a dhukbe na)
            do this

        example:prime number

        a=int(input())
        b=int(input())
        s=range(a,b)
        for x in s:
            for num in range(2,x):
                if x%num==0:
                    break
            else:
                print(x,"is prime number")



