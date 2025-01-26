#identifiers

->> the smallest identifying unit in the program is calles identifier

->> an identifier can denote various entities like variables, types, labels, subroutines or functions, packages and so on.

#variables

->> variables are nothing but reserved memory location to store value

->> this means that when you create a variable you reserve some space in memory

->> while the program is running, variables are accessed and sometimes changed, i.e. a new value will be assigned to the variable

->> declaring a variable means binding it to a data type(in strongly typed languages like c,c++,java,etc)

->> you don't need to declare variables before using them or declare their type
->> if there is need of variable, you think of a name and start using it as a variable


#variable naming rules

->> combination of alphabet,digit and underscore

    x=value
    x9=value
    x_9=value
    _x=value
    _0p=value

->> can not start with digit

    9p is not possible
->> case sensitive

    x and X different
->> keywords can not be used as variable

    int,flaot etc. can not use


#dynamically typed variable

->> not only the value of a variable may change during program execution but the type as well

->> you can assign an integer value to a variable, use it as an integer for a while and then assign a string to the variable

#finding variable type

->> we use type() function

    type(variable_name)

#finding variable address

->> we use id()function

    id(variable_name)

#object

->> object is something which is capable to store set of values and can invoke set of operations

->> every variable in python is an object