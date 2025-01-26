# Arithmetic operator

    operator    expression_example  name

    **              3**2          exponent
    /               10/5     divide(float)
    //              5//2      floor divide
    *               5*4           multiply
    %               10%4           modulus
    +               5+2           addition
    -               5-2        substaction

1. jokhon amra choto songkha k boro songkha diye mod kori ans choto songkha hobe

        5%10==5

2. jokhn amra choto songkha k boro songkha diye floor kori ans zero ashbe

        5//10==0

3. +,* we can use also in string. + korle concat hobe but both string hote hobe r * korle repition hobe
    
        "10"+"5" //concat//"105"
        "10"*3 //repitition//"101010"

![](<op diagram.drawio.png>)

# Relational operators

    operator    expression_example  name

    >           3>2       greater than
    <           10<5         less than
    >=          5>=2 greaterthan or equal 
    <=          5<=4    less than or equal
    ==          10==4           equal
    !=          5!=4            not equal


- they always yield true or false as a result

- when true value converted to int, it becomes 1 or 0

- they can be used to compare strings

- Only == and != can work between complex value

# Logical operators

    operator    expression_example  work

    and          a>b and a>c    all true then true   

    or           a>b or a>c     all false then false

    not          not a>b        inverse the result


- logical operators must be written in lowercase only

- non zero operand will be treated as true, zero will be treated as false

- empty string is always false. non-empty string is true


# Bitwise operators
- The Bitwise operator are AND, OR, XOR, Complement, Left shift , Right Shift.

- These operators work on integral type of data and they perform operation on Binary representation of data I.e, 0’s and 1’s.

- Bitwise operators are used in applications of networking , Encryption and Decryption etc.

- Bitwise calculations starts from right hand side.

        operator    expression_example 

        & (and)         5&6=4
        |(or)           5|6=7
        ~(not)          ~5=-6      
        ^(xor)          5^6=3
        >>(right shift)
        <<(left shift)
## Understanding Binary numbers system :
- To understand bitwise we first need to understand binary number system . Binary number system uses only 0’s and 1’s

- Decimal number system uses numbers from 0 - 9

- To convert decimal to binary we can do it in either 2 ways
## work of "&"

      0&0=0
      0&1=0
      1&0=0
      1&1=1

      5&6=4:expalin,
           5=101
           6=110
           ------
             100=4

## work of "|"

      0|0=0
      0|1=1
      1|0=1
      1|1=1

      5|6=7:expalin,
           5=101
           6=110
           ------
             111=7

## work of "^"

      0^0=0
      0^1=1
      1^0=1
      1^1=0

      5^6=3:expalin,
           5=101
           6=110
           ------
             011=3

## work of "~"

      ~0=1
      ~1=0

      ~5=4:expalin,
                                5=101
        then add zero before binary   0101

        then 1's complement           1010  

        then 2's complement             +1
                                    --------
                                       110=6
                                         =-6  





## work of right shift ">>"
- a = 10 ( binary of 10 = 1010 )
- If we left shift ‘ a ’ by one place I.e, a << 1 then

            1 0 1 0
          1 0 1 0 0 Left shift by one place & Extra space filled with value zero
- After left shift by one place the bit that is freed will be taken as zero.
        
        Now 10100 = 20 = 2* 10
- If we left shift 20 again then,

                  1 0 1 0 0
                1 0 1 0 0 0 = 40 = 2 * 20
- We see that when we left shift the number will double for one place I.e; a << n , a * 2 ( power n)

- If we double the left shift I.e , a. << 2 then

            a << 2 = 2( power n ) * a = 4*10 = 40
- similarly , if we do a << 5 , then the value gets double for 5 times

        a << 5 = 2( power 5 ) * a = 32 * 10 = 320

## work of right shift ">>"

- If we RIGHT SHIFT the number will become half.
        
        a = 10 -> 1 0 1 0
                 __ 1 0 1  ( this 0 gets discarded )
        This leading empty space has no value ( it becomes zero )
- Right shift operator divide by 2 I.e;
        
         a >> n= a / 2 ( power n )

# Assignment operators

    operator    expression_example
    =               x=5
    +=              x+=5
    -=              x-=2
    *=              x*=2
    /=              x/=3
    %=              x%=2
    //=             x//=5
    **=             x**=5
    &=              x&=3
    |=              x|=2
    ^=              x^=3
    >>=             x>>=2
    <<=             x<<=2

# Identity operators

- the is operator: it return true if both var are the same object

      x=5
      y=5
      here every var is object. object are dynamically created. object do not have names but references
      so here there is not created two space in memory,it creats one space and x,y refer that space

      x==y= true if value is same
    
      x is y= true  if reference is same

- the is not operator: it return false if both var are the same object

- if x and y take same value from user without typecasting then there value is same but reference is difference

# Membership operator

- the in operator: it return true if a sequence with the specified value is present in the object

      x="abc"
    
      here x must be iterable that means collection of data

      "a" in x
      "A" in x
    

- the not in operator: it return false if a sequence with the specified value is present in the object

      x="abc"
    
      "A" not in x
      "a" not in x


# Expressions 
- precidence

         () > Func_call > slicing > exponent > mul,div,mod > add,subs

- if precidence is equal the go through left to right




