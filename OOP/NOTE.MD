# Programming way
1. Procedure(function) oriented way of programming
2. Object(data+function) oriented way of programming 
    - for large program
## Main aspects of OOP
- Classes and Object
- Inheritance
- Polymorphism
- Data Hiding

### Class and Object
- assume,

    - common noun as class &
    - proper noun as object

    - exmaple:

            dr.bindra, dr. mamun

            here, 
                dr. is class
                dr.bindra is object of dr. class
                dr.mamun is object of dr. class

#### what is class?
- class is a keyword
- class has some name
- class encapsulates data and function
- creating class is creating type
- class is a description of an object
- class is a blueprint of an object
- int,float,complex,str,tuple,dict,set,list etc are built-in classes
- it defines various attributes of an object.

    #### syntex

            class className():
                
                attributes(properties & methods)
            

    #### attributes:

    - attributes are member variables and member functions
    - variables two type
        - instance variable
            - it can create in init() method,instance method and outside of class(objname.varName)
        - static/class variable
            - it can access from init() method using className.staticVarname

    - example:

            class test:
                x=5 
                def f():
                    some code
            
            here, x and f() are attributes & x is static variable
            

            ramesh(noun).running(verb)
    
            - here, ramesh is noun which is work as object & running is verb which is work as action it also known as function

            - this function is known as methods

            - ramesh(object) can use those function(method) which is include in class


#### what is objcet?
- object is something which can store its properties(variable) and capable to perform some action
- object is an instance(example) of a class
- instance=object
- you can create any number of objects of some class, but you have to define class first
- objects are two type

    1. class object
    2. instance objcet

    #### syntex:

        object_name=class_name()

    #### type of object:

    - test vs test()

        - test represent the reference of class and also known as class object . it denote by class name & test() represent function call and create instance object

        - one class has only one class object but can have many instance object

        - example:

                class test:
                    do something
                
                obj=test()
                obj1=test()
                test.attributes

                here test is class object and obj,obj1 are instance object.

    - the variable which is include in class object called class object variable (static variable) & which is include in instance object called instance variable







#### __init__() method:

- instance object works start from here. when we create an object then autometically it call __init__() method.

- all the work under this method called instance work

- must create minimum one parameter and it can any name but we always use self. self parameter it store the reference of the object

- when we create any variable we use self.var_name

- syntex:

        class class_name:
            def __init__(self):
                self.var_name=value

        this var_name is instance variable
- it's also known as constractor

#### methods:

1. instance method

        def method_name(self):
            pass
2. static method(we use it for different work . not specific object work or class work)
    - Instance method access instance variable,class method access class variable.
    - This methods are like global function.if there is any relation in the class we can put inside the class.
    - The staticmethod() returns a static method for a function passed as the parameter
    - syntex

            @staticmethod
            def method_name():
                pass
3. class method(to access class/static attributes)

        @classmethod
        def method_name(cls):
            pass

#### calling methods

1. instance method

        instance_object.method_name()

        
2. class method
  
        class_name.method_name()
        instance_objectName.methodName()
3. static method

        class_name.method_name()
        instance_object.method_name()

#### Accessors(read) and Mutators(write)
- get() to get value and set() to modify the value method follows the accessors and mutators

        def getValue(self):
            return self.value
        def setValue(self,value):
            self.value=value
### Inheritance
- defining a new class with the help of an old class is called Inheritance.

- reusability

- here is relation between parent(base/super/old) class and child(sub/new/derived) class

    #### syntex
            class Base:
                ....
            class Derived(Base):
                def __init__(self,parameters):
                    super().__init__(parameters)

                    or

                    Base.__init__(self,parameters)

            eg.

            class person:
                def __init__(self,name,age):
                    self.name=name
                    self.age=age
                def showName(self):
                    print(f"Name= {self.name}")
                def showAge(self):
                    print("Age=",self.age)
            
            class student(person):
                def __init__(self,roll,name,age):
                    super().__init__(name,age)
                    self.roll=roll
                def showRoll(self):
                    print("Roll number=",self.roll)
            
            s=student(100,"amit",15)
### Inner/Nested classes
- It means we can define class in another class.
- Means class can have class as it’s members just like a class can have attributes and methods
- similarly a class can also have a class as it’s members.
- Let us write class for customer:

        class Customer:
            def __init__(self,id,name,bdno,bstreet,bcity,bcountry,bpin,sdno,sstreet,scity,scountry,spin):
                self.custid=id
                self.name=name
                self.billingAdd=self.Address(bdno,bstreet,bcity,bcountry,bpin)
                self.shippingAdd=self.Address(sdno,sstreet,scity,scountry,spin)
            
            class Address:
                def __init__(self,dno,street,city,country,pin):
                    self.dno=dno
                    self.street=street
                    self.city=city
                    self.country=country
                    self.pin=pin
                def display(self):
                    print(self.dno,
                    self.street,
                    self.city,
                    self.country,
                    self.pin)
        
        c=Customer(10,"mamun",101,"abc","dhaka","bd",1001,200,"ijk","khulna","bd",4001)
        c.billingAdd.display()

        output:
        101
        abc
        dhaka
        bd
        1001

### Polymorphism
- Polymorphism: many functions
- Polymorphism means One name(function) different actions
#### Duck Typing
- Driver is a function who is driving the car and running cars.. so it is the example of polymorphism
a driver can use or run multiple cars means different actions and forms but same function

        def Driver(car):
            car.drive()
        
        class Creta:
            def drive(self):
                print("creta is driving")
        class Marcedes:
            def drive(self):
                print("Marcedes is driving")
        
        c= Marcedes()
        Driver(c)

#### Method Overloading
- Method overloading is used for achieving polymorphism
##### What is polymorphism:
- One name different actions or multiple actions
- Python supports overloading writing one method which can act differently in different situations.
##### How python supports overloading ?
    Class Arith:# creating class
        Def sum(x, y)# takes two parameters
            Return x+y # returning parameters by adding
    a= arith()
    print(a.sum(10,5))# calling sum
    print(a.sum(8.5, 7.6))
    print(a.sum(“Hello”, “world”))
- It is adding int, float , string it is nothing but we are achieving polymorphism
- Python supports overloading implicitly.

##### Error
- Python does not allow two methods using same name.
- It will try to call out the second method and shadowed the second method
- We can never call the first method by calling two parameters

        class Arith:
            def sum(self,a,b):
                return a+b
            def sum(self,a,b,c):
                return a+b+c
        a=Arith()
        print(a.sum("hello","world"))
        print(a.sum(5,10,3))
##### How single parameter works for both 2 and 3 parameters
    class Arith:
        def sum(self,a,b,c=None):
            s=a+b
            if c==None:
                return s
            else:
                return s+c
    a=Arith()
    print(a.sum(5,10,6))
    print(a.sum(8,9))
- So python is having method overloading implicitly
- We don’t have to write multiple methods with the same name but the single method can
behave in different type of method.

#### Method Overriding
- Redefining the method of parent class in child class is said as method
overriding
- In other words, the child class has access to the properties and functions of the parent class method while also extending additional functions of its own
to the method.
        
        Class iphone6:
            def home(self):
                print("home button is pressed")
        Class iphonex(iphone6):
            def home(self):
                print("home is touched)
                super().home()
- iphone x is newly designed phone . It is inheriting the features of iphone6. but it is having new home method . it is not borrowing the method (iphone 6) as it is because they was not physical button
- Both have home method . But the child method will be called .parent method will be shoddowed. we cant all it directly.To override the Parent Class method, you have to create a function in the Child class with the same name and the same number of parameters.
- The child class should have the same name and the same number of parameters as the parent class.
- For self: to call a function firstly we have to create a variable then we can call the function

- Example : ph = iPhone(6)——-function calling
- ph.home() ——-method calling
- You can’t use super outside the class .method overriding cannot be
performed in the same class, and overriding can only be executed when a
child class is derived through inheritance.
- super() home() ——— this is how parent method is called . So it should be called inside the class

#### Operator Overloading

- Operator Overloading is where operators behave differently in different
situations
- Operator Overloading is possible in normal DataType also
- Using operators we can achieve polymorphism
- Lets see this with an example
- We can add 2 rational numbers using operator overloading

        class retional:
            def __init__(self,p=1,q=1):
                self.p,self.q=p,q
            def __add__(self,other):
                s=retional()
                s.p=self.p*other.q+self.q*other.p
                s.q=self.q*other.q 
                return s 
            
        r1=retional(2,3)
        r2=retional(2,5)
        sum=r1+r2 

- You can also overload for subtraction , multiplication , power , division etc.
• Operator Overloading also works well for comparison operators and
assignment operators.

### Abstraction
- eta class er vetorer data and method k class er baire theke obanchito access hote surokkha prodan kore.

### Encapsulation: 
- er meaning goponiota. onno kono object theke kono class er data lukano ba direct use theke biroto rakha ee encapsulation. orthat kono class er data ba method k private kore rakhar prokriya ee encapsulation.

### Message Passing 
- programmer proyojone object er moddhe porospor call korar prokriya k message passing bole

### Dynamic Binding 
- je prokriyangsho gulo dynamic reference er vittite program nirbaher somoy upojukto class er object select er maddhome shothik method select kora hoy ba ek method theke onno method a sthanantor kora hoy take dynamic binding bole.

### Open Recursion
- kono method nijei nije ke call korle take recursion bole. recursion use korar permit dey