# What is function ? 
# It is a programming construct that return output if i give some input.
# 2 types--
# Built in function -- print(), type(),input().
# user define  -- user desired function .
# 
# Abstruction -- Have someting but not visible.
# Decomposition -- Multiple function working to built the system. 
# 
# Component of function --
# def keyword -- means function 
# def ---Name_of_function (input):
#  """Docs string-reading manual"""
# line of code
#  return output 
# the n do amke a call of the function #


# Function creation   __ Inputed place call parameter during creation 
def odd_even(number):
    """
    It's check the given number is odd or even. 
    input - any valid integer .
    output- odd/even.
    created on - 3rd sep 2026
    """
    if type(number)== int :
        if number %2==0:
            return "even"
        else:
            return "odd"
    else : return "Are you mad ?"

# To see the documentation --
print (odd_even.__doc__)

# Function call -- Function_name(input)-- Inputed place call argument during insertion.

for i in range (1,11):
    x=odd_even(i)
    print (x)

print(odd_even("hello"))


# There is 2 point of view - 1) Creating a function 2) Using a function

# Types of arguments 
#    * Default Argument -- 
#    * Positional Argument --  
#    * Keyword Argument -- 

# Default Argument -- A default argument is a value that is automatically used 
# by a function if the user does not provide a value for that parameter.

def power(a=1,b=1):    # If the value of a/b not given the assume then the value will be 1    
    return a**b

print (power (2,3))     # 8
print (power(2))        # 2 
print (power())         # 1

# Positional argument -- A positional argument is an argument that is passed to a function based 
# on its position (order) 

print(power(2,3))   # the order send value by the argument the same way the parameter receive it.


# Keyword Argument --  at this point the parameter ius called keyword
print (power (b=3,a=2)) # position doesnot matter,just want the value of a and b to the right parameter
                        # Good for multiple parameter.


# *args and **kwargs -- are special Python keyword that are used to pass the variable length of arguments to a function.

# *args 
# Allows us to pass a variable number of non-keyword arguments to a function.


# Here if we want to multiply once 2 variable next 10 varibles then we need to recreate the function but using the 
# args it's not necessary.
 
def multiply (a,b,c,d):
    return a*b*c*d

print(multiply (7,9,5,4))

def argsmultiply(*args):         # It's create a tuple internally the finish operation.
    product =1
    for i in args:               # If the value range is known then use range otherwise use the variable
        product= product*i
    print (args)                 # tuple-- proof 
    return product 
print (argsmultiply(1,2,3,4,5,6,7,1,2,3,3,0))   # Mulitiple  inputed value but calculated easily without recreat the function.


def argadd(*sarwar):
    result =0
    for i in sarwar:
        result += i
    print (sarwar)
    return result

print ( argadd(1,2,3,4,5,6,7))

# Watch documentation 
# print(print.__doc__)
# print (type.__doc__)

#  **kwargs
#  **kwargs allows us to pass any number of keyword arguments
#  keyword arguments mean that they contain a key-value pair , like a python dictionary.

# Function work - countries and the capitals print 
def display(**kwargs):     # here kwargs become dictionary
    for (key,value) in kwargs.items():
        print (key,"->",value)

display(Bangladesh='Dhaka',Srilanka='colombo',Nepal='katmandu')

# Points to remember while using *args and **kwargs  --
# order of the arguments matter (normal parameter -> *args ->**kwargs )
# The words "args" and "kwargs" are only a convention , we can use any name of our choice.


# How functions are executed in memory ?? -- use Python visualizer 
# A function is active in RAM between the Call and return .
# It's acts  like a independent program and has own lifespends in memory .

# Without return statement
# Even though if we don't use the return in a function it's return a default  "None"  for call that.  
l=[1,2]
print(l.append(5))   # It's add the value 5 to the list but doesnot work as return so it's default is None.
print(l)             # print function return something .


# Variable Scope 
# GLobal variable vs Local variable 

# Those variable who are in program scope are global variable.
# Those variable who are in function scope are local variable.#

def g(y):         # Here , y is function variable so local variable . Main program cannot use the local variable.
    print(x)      # Global using in local.
    print(x+1) 
x=5               # Here , the x is program variable so it's a global variable. Function can use the global variable.
print(g(x))       # Return is None
print(x)          # N.B: Local variable with the same name of global variable → usually does not change the global variable. it's expect to change the local .


# A function is work as independent program. so local variable and global variable same name doesnot make any issue. They are identical twin. 
def f(x):
    x=1
    x+=1
    print(x)
x=5
f(x)
print(x)


def h(y):
    print(y)
    # x+=1       # In a function if any variable doesnot exit but has as global then can use but not allow to change .
                 # Otherwise, issue appears.
x =5              
h(x)
print(x)    



def h(y):
    print(y)
    global x        #  Should not use global variable . It's not a good practice. 
    x+=1            # You have to use it responsibility.


x =5              
h(x)
print(x)  

def f(x):
    x=x+1
    print('in f(x) : x=',x)
    return x
x=3
z=f(x)
print('in main program scope:x=',x)
print('in main program scope:z=',z)

# Nested function 

def f():
    def g():
        print('inside function g')
    g()
    print('inside function f')
f()        
# g()       - Error 


def g(x):
    def h():
        x='abc'
    x=x+1
    print ('in g(x): ',x)
    h()
    return x
x=4
z=g(x)


def g(x):
    def h(x):
        x=x+1
        print('in h(x):x =',x)
    x=x+1
    print ('in g(x):x =',x)
    h(x)
    return x
x=3
z=g(x)
print ('in main program scope x =',x)
print ('in main program scope z =',z)


# Function are 1st class citizens ---
# means it can be stored in variables, passed as arguments, returned from functions, 
# and manipulated like any other value.

# type amd id          --- function in python is a datatype like int, list etc

def square(num):
    return num**2

print (type (square))
print (id(2))
print (id(square))

# reassign 

x=square                # Function copied to x (rename)-- check id 
print (id(x))
print (x(3))            # Result : 9

# deleting a fucntion 
    # del square 
    # print (square (2))            # Square function deleted so error.
    # storing

# Storing 
l=[1,2,3,4,5,square]
print(l)
print (l[-1](3))                  # 9


s={square (3)}                    # The code is working so function is  immutable 

# returning a function
def f():
    def x(a,b):
        return a+b
    return x                 # It's return a function  f()=x=x(a,b)=x(3,4)  tricky
val=f()(3,4)
print (val)

# Function as arguments

def func_a():
    print ('inside func_a')

def func_b(z):
    print ('inside fun_b') 
    return z()

print (func_b(func_a))

# Benefints of using a function
 # Code Modularity   -- separate code 
 # Code Readibility  -- 
 # Code Reusebility

# Lanbda Function
 # A lambda function is a small anonymous(no name) function.
 # A lambda function can take any number of arguments , but can only have one expression. 
 # lambda a,b: a+b   lambda keyword / a,b parameters (can more) : Expression (only one)

# x -> x^2
a = lambda a : a**2    # Have to save in variable 
print (a(2))

# x,y -> x+y
a= lambda x,y : x+y
print (a(4,56))

# Diff between lambda and Normal Function 
    # No name 
    # Lambda has no return value (infact, return a function)
    # Lanbda ia written in 1 line
    # No reusable 
# Then why use lanbda function 
# They are used with HOF -- Higher order function 
                # The function that return a function or receive a function as input .

# Check if a string has 'a'
a = lambda s: 'a' in s 
print (a('hello'))

# odd or even
oe = lambda x: 'even' if x%2==0 else 'odd'
print (oe (34))
print (oe (33))

# HOF
def square (x):
    return x**2

def cube (x):
    return x**3
    
def transform (f,L):          # This is a HOF 
    output = []
    for i in L:
        output .append(f(i))
    print (output)

L= [1,2,3,4,5]
print (transform (square , L ))

# Rather than creating and sending fuction square and cube use lambda .

print (transform(lambda x: x**3 , L))        # Short use of Function as HOF 


# MAP

# Square the items of a list 

L= list(map (lambda x: x**2 ,[1,2,3,4,5]))
print (L)                    #  [1, 4, 9, 16, 25]

# Odd / even labelling of list items 
L = [11,12,13,24,45]
Ls=list (map (lambda x: 'even' if x%2==0 else 'odd',L ))
print (Ls)

# Fetch names from a list of dictionary 

users = [
    {
        'name': 'Rakib',
        'age' : 15,
        'gender': 'male'
    },
    {
        'name':'Rahat',
        'age':16,
        'gender': 'male'
    },
    {
        'name':'khairat',
        'age':33,
        'gender':' female'
    }
]

genderofusers = list(map(lambda users : users['gender'],users)) 
print (genderofusers)
nameofusers = list (map ( lambda dict: dict ['name'],users))
print (nameofusers)
ageofusers = list (map ( lambda dict: dict ['age'],users))
print (ageofusers )

# Filter - Have condition 

# Numbers greater than 50
L = [10,30,60,55]
filternumber=list(filter(lambda x:x>50,L))
print (filternumber)

# Fetch fruits starting with 'a'
L= ['apple','banana','cherry']
fruitofstarta= list(filter(lambda a: a.startswith('a'),L))
print( fruitofstarta)

# Reduce
 # functools.py - Tools for working with function and callable object 

import functools
sum= functools.reduce(lambda x,y: x+y,[1,2,3,4,5,56,778,88] )
print(sum)

# Find min
minnumber= functools.reduce(lambda x,y: x if x<y else y , [1,2,3,0,8,6])
print(minnumber)

# find max 
maxnumber =  functools.reduce(lambda x,y: x if x>y else y , [1,2,3,0,8,6])
print (maxnumber )

# Automatic saving failed. This file was updated remotly or in another tab./

