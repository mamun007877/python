# Introduction to string
- Anything written inside ‘ ’ , “ ” in quotes is called string
- String can contain english alphabet ,special characters like @ - \. / # ( ) , it can
also contain characters from other languages also
- In memory strings looks like an array of Character it has +ve and -ve indexing as well
- When you call an input function normally it'll give string by default
- len( ) gives you length of a string
- We can use for loop for accessing every element in a string
- When a string value is given directly in the program then its called string literals
- String literals can be in ‘ ’ , “ ” , ‘’ ‘’ , “” “”
- When a string already contains a single quote ( inner quotes ) then you should enclose the
string in double quotes (outer quotes ) and vice versa
        
        Ex : s = “ John ’ s ”or
        S = ‘ John ” s ’
- If a string is in multiple lines then you have to use triple single quotes (or) triple double quotes
        
        Ex : ‘ ‘ ‘ hello
        How are you ’ ’ ’
        or
        “ “ “ hello
        How are you ” ” ”

# Operators on String
1. Concatenation :

        s1 = ‘ hello ‘
        s2 = ‘ world ‘
        s3 = s1+ s2
        s3 = ‘ helloworld ’
    - It will concatenate the two string and gives the new string . Because string is immutable it will not modify it . It will create a new string

            s4 = ‘ hello ‘ ‘ world ‘
            Output : hello world
            s5 = ‘ hello ‘ + 15 #error

    - We have to do type casting with string

            s5 = ‘ hello ‘ + str(15)
            Output : hello15
2. Repetition
  - It will repeat

            s1 = ‘ hi ‘
            s1 * 3
            Output : hihihi

            **But the thing is it should be integer
  - You can have same string multiple times by using multiplication

            s1 * 2.5
3. Indexing :

        s1 = ‘ hello world ‘
    - You can access any character of the string using index also called as substring

                s1[ 4 ] —— o
                s1[ 6 ] —— w
                s1[ -5 ] —— o
4. Slicing :
            
            s1 [start : end : step ]
    - Slicing will work just like loop
    - To print a string in reverse we use -ve indexing , starting from -1
    - Suppose if a string stops at -11 [ n ] then we should write -12 [ n-1 ] in the slicing operator to get -11.
    - If we do not give an end point in slicing it takes the default value (I.e, where the list ends ) automatically , same goes for start point (default is 0) and stepsize (default is 1).
    - Instead of using range based for loop we can use slicing to get the same result.
    -Slicing gives a separate string.

                s1= ‘hello world ‘

                s1[0:len(s1):1]
                output=hello world

                s1[:len(s1):1]
                output=hello world

                s1[::1]
                output=hello world

                s1[::]
                output=hello world

                s1[3::]
                output=lo world

                s1[::2]
                output=hlowrd

                s1[0 : len (s1) : 1 ]
                Output : hello w

                s1[-1:-len (s1)-1 :-1]
                output=dlrow olleh

                s1[-1::-1]
                output=dlrow olleh

                s1[-1::2]
                output=drwolh

5. in :
    - It will say if a character is present in the string or not . If it is present then it will return True or else False .

                h in s1 —— True
                world in s1 —— True
                me in s1 —— False
6. not in :
    - It will say if it is not present . Then it will return True or else False .

                me not in s1 —— True
                world not in s1 —— False •

# Introduction to string methods
- The string is a built - in class in python
- Classes contains definition / design ( there are of 2 types data and operation / methods )
- Objects is an instance of that definition design
- In string many member function are available these member functions are called string
methods
- To know all the methods present in string class we can type a function called dir( str ) it shows
all the method
- You can access all the methods using dot ( . ) operator (or) just want to know about particular
method

        Ex : s = ‘ hello’
        help( s.endswith )

# String Method
- Methods are the member of the class which performs operation upon the data of an object
        
        S = “ hello, how are you “

1. s.find ( sub [ , start [ ,end]]). it will return index of the first occurrence of the string.

    - sub ( find the occurrence of the substring )
    - Methods are called by using object name that is variable name

            s.find(‘o’)

                - It will start looking for o from the left hand of the string . The result is 4 cause we found ‘ o ‘ there

            s.find (‘ how ‘)

                - The result will be 7

            s.find(‘ k ‘)

                - The result will be -1 . Why it is -1 because the character will start from 0 . -1 means outside the range . So it is invalid position .

            s.find ( ‘ o ‘ , 5 )
                      sub start
                - If you want to find out after the 5th index we write 5 in starting index
                - If you want to find out other substring then you should give starting and ending index

            s . find (‘o’ , 5 , 7 )
                - It will check from 5 to 7
                - You can pass the find by single , double or 3 parameters
2. s.rfind ( sub [ , start [ ,end]])
    -It is same as find but in find we where searching from left but in rfind will search substring from right
    
        s.rfind(‘o’) 16 index
        s.find (‘o ‘ , 0 , 15 ) 8 index
    - In rfind ending index will work but in find starting index will work
    - -1 will return if its out of string
3. s.index ( )
    - s.index and s.find is same but have minor differences . rindex is same as rfind
4. s.count( )
    - It will count the number of occurrence
    - Lets take an example - character ‘ o ‘.‘o’ it repeated 3 times
    - The count gives counting of the string. It will not gives all the indexes . It will only count

# summary

            s.find ( ‘ k ‘ ) -1
            s.index (‘ k ‘ ) substring not found
            s.rindex( ‘o ‘ , 0 , 15 ) 16
            s.count (‘me’) -0
            s.count(‘how’) -1

# String Method #2

5. s.ljust(width[,fill])
6. s.rjust(width[,fill])
7. s.center(width[,fill])
- This methods are useful for text alignment
        
        s = ‘ python ‘
- If you want to write in extra spaces like 10 spaces
               
                s.ljust ( )
                s.rjust ( )
                s.center ( )
- If the string is larger than the spaces given by using
                
                s.ljust(3)
                        - It will take the entire string it will not just take 3 letters
                        - If you want bigger space you mention the width bigger than the length of the string
                        - All this have one more parameter that is fill
                
                s.center(10 , ‘ * ‘ )
                        - Python have only 6 alphabets but we want 10 spaces . * will be filled in empty spaces
                        - 10 space vacant spaces with * otherwise it will fill with spaces
                
        
- String is immutable so it will not modify it will create a new string

8. s.strip ([ chars ])
9. s.lstrip ([ chars ]) this is useful for removing the characters from the string
10. s.rstrip ([ chars ])
- They remove leading char , tailing characters and characters from both sides … by default they
will remove spaces
        
        s.lstrip - it will remove leading char
        s.rstrip - tailing removes character
        s.strip - removes spaces from both the side S = ‘ ……….. ……… ++aaaapython ‘
        s. lstrip (‘ . ‘ ) ———> it will remove leading dots and stops when there is no dot
        O/p - ‘ ………++aaaapython ‘
        s.lstrip(‘ . + ‘ ) ———> it will remove dot spaces and +
        O/p - ‘aaaapython’
- All this methods will return new string they will generate new string after performing the
operations

# String Methods #3
- The methods we are discussing here are

11. s.capitalize( )

        s="hello dear" s.capitalize() ->>"Hello dear"

12. s.lower( )

        s="HeLLo" s.lower() ->> "hello"
13. s.upper( )

        s="HeLLo" s.upper() ->> "HELLO"
14. s.title( )
- s.title( ) , here first letter of every word in a string becomes capital

        s="hEllO deAr" s.title() ->>"Hello Dear"
15. s.swapcase( )

        s="HEllO" s.swapcase() ->>"heLLo"
16. s.casefold( )
- s.casefold( ) , It converts string into lowercase letters as s.lower( ) but there are some
difference between them

        s="HELLO" s.casefold() ->> "hello"

# String Methods #4
17. s.isupper( )
18. s.islower( )
19. s.istitle ( )
20. s.isalnum ( )
21. s.isalpha ( )
22. s.isspace ( )
23. s.isascii ( )
- It will return in boolean result ( T or F )
        
        
        s = ‘ HELLO ‘
        s.isupper( )
                - It will return true if only all the alphabets are in capital letters
        
        
        
        s = ‘ hellO ‘
        s.islower( )
                - It will return false because all should be in lower case but in this O is capital so its false
        
        
        
        s = ‘ How Are You ‘
        s.istitle ( )
                - Every starting letter should be capital so it will return True and empty string will return False .
        
        s.isalnum ( )
                - If the string contain alphabets and numbers it will return true . If it contain special alphabets
                than it will return false
        
                        s = ‘ abc-123’ — — > False
        
        s.isalpha ( )
                - If it is only alphabets then it will return true
        
                        s = ‘ abcd ‘ ——> True
        
                        s = ‘ abcd123’ — — > False
                - This alpha and album works on any language
        
        s.isspace ( )
                - It will check if there are any spaces present in the string then it will return true
        
                        s = ‘ hello world ‘ ——> True
        
        s.isascii ( )
                - If it contain all the ASCII character , can have lower case , upper case , special character etc
                then it will return True

                        ‘ abc12#! ‘ ——> True
        
                        s ——> True #empty string will return True 


24. s.isidentifier( )

        s = ‘ length1 ‘ ——> True
        s = ‘ 1length ‘ ——> False
- Variable can not Start with a number so it will return false
- This method will check if it gives the valid name of the variable
- For keywords also it will return true
        
        s = ‘ if ‘ ——> True
25. s.isprintable( )
- All the ASCII letters , other language letters are printable but there are escape characters \n \t \r
are not printable so it will return false
        
        s = ‘ hello ‘ ——> True
        s = ‘ hello \n how are you ‘ ——> False
26. s.isdecimal( )
- It will say of there are decimal present in the string
        
        s = ‘ 125 ‘ ——> True
        s = ‘ 1.25 ‘ ——>False
- What are decimal ?? Decimal are the numbers between 0 - 9
27. s.isdigit( )
        
        s = ‘ 1682 ‘ ——> True
- If you have special numbers it will return true
- But in s.isdecimal ( ) it will return False
27. s.isnumeric( )
        
        s = ‘ 5 1/2 ‘ ——> True
- But in decimal and digit it will be false
- It will return true to any number





28. S.replace(old, new,[,count])
                
                1. s=‘a-b-c-d-e’ want to replace all these hyphens with commas using these methods
                
                   S.replace(‘-’ ‘,’ 3)
                
                   So the first one is old and the next one is new
                
                   ‘a, b, c, d-e’->This is a new string modify the old string and generate new string
                
                    We can mention the count but it is optional
                
                2. s='a-b-c-d-e'
                
                   s.replace('-', ‘,’)#replacing it with comma
                
                   s='a,b,c,d,e'
                
                3. s='a-b-c-d-e'
                
                   s.replace('k','m')
                
                  'a-b-c-d-e'
                
                4. s='abcd@gmail.com'
                
                   s.replace(‘gmail’,'yahoo')#replacing it with yahoo
                
                   ‘abcd@yahoo.com'
                
                This is the replace method
29. s.join(iterable)
- The join method:
                
                s1='xyz'
                
                s2='abc'
                
                s1.join(s2)# calling s1 method and joining upon s2
                
                'axyzbxyzc'
                
                s1='/'
                
                s1.join(s2)# letters of s1 and s2 as a separator
                
                'a/b/c'
                
                So, the parameter is string so its taking letters of a string
30. S.split([sep[, max split]])

- The split method:
                
                s='john smith ajay'
                
                s.split()# it splits['john', 'smith', 'ajay']
                
                s.split('h')
                
                ['jo', 'n smit', ' ajay']
                
                s.split(',')
                
                ['john smith ajay']
                
                s='john-smith-ajay-khan-james'
                
                s.split('-')
                
                ['john', 'smith', 'ajay', 'khan', 'james']
31. S.rspli([sep[, max split]])

- The s. rSplit method:
-The s. Split means splitting is done from right hand side

32. s.splitlines([keepends])
S.splitlines works same as split only
        
        s=‘aaa\nbbb\tccc\rddd\feee
        s.splitlines()
        ["aaa","bbb\tccc","ddd","eee"]

# special function for string

1. sorted(string)
        - returns a sorted list of strings