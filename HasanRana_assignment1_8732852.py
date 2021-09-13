# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:12:31 2021

PROG 8420                                    
Programming for Big Data 
Radha Chawla
Assignment 1
_______________________________________________________________________________ 

Written by Hasan Mahamud Rana
ID: 8732852                               
_______________________________________________________________________________

"""

"""
-------------------------------------------------------------------------------
Question 1: Write a python program to display the multiplication table with 
taking input from the user. [5 marks]
-------------------------------------------------------------------------------
"""

Num = int(input('Enter the Number: '))                   # Take input from user

for i in range(1,11, 3) :                                   # Call a for loop with range 10                   
    print('{} X {} = {}'.format(Num, i, Num * i))        # Print result

"""
Reference
Radha Chawla. (2021). PROG8420_Week 4_Object type part 2 slide 3 [PowerPoint slides]. eConestoga.

"""


"""
-------------------------------------------------------------------------------
Question 2: What are functions in python and what is the purpose of them? [2 marks]
-------------------------------------------------------------------------------

Answer: A function is a group of related organized statements that are writing to perform 
a particular specific task. A function is a block of code which only runs when it is called.

We can pass data, known as parameters, into a function.

There are inbuilt functions i.e print() and also user-defined functions.

Function purpose:
We can use it repeatedly.
Maximizing code reuse.
The function also provides procedural decomposition. We can decompose multiple 
extensive procedures and divide them into various groups or considerable chunks.
The function makes a program much easier to understand.
 

Creating a Function, In Python a  user-defined function is defined using the def keyword:
# Syntax

def <name>(arg1, arg2,... argN):
    <statements>
    return(<value>)

"""    
    
# Defining a Function
def my_function():
  print('Hello from a function')


# Calling a Function
# To call a function, use the function name followed by parenthesis:

my_function()

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

#Example
def my_function_with_arguments(x, y):
    z = x ** y
    return(z)

x = 2
y = 3
result = my_function_with_arguments(x,y)
result

"""
Reference
Radha Chawla. (2021). PROG8420_Week 6_W6 - 02 - Func [PowerPoint slides]. eConestoga.

"""

"""
-------------------------------------------------------------------------------
Question 3: Write a program to check odd or even number. [5marks]
-------------------------------------------------------------------------------
"""
def evenOdd(num):
    if (num % 2) == 0:
       print('{0} is Even number'.format(num))
    else:
       print('{0} is Odd number'.format(num))


num = int(input('Enter a number to check odd or even: '))
evenOdd(num)

"""
-------------------------------------------------------------------------------
Question 4: What are lists and how are they different from tuples with example? [3 marks]
-------------------------------------------------------------------------------
"""
# List
# To create a list in Python, enclose items in square brackets separated by commas and 
# assign it a variable.

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(weekdays)

# A tuple is an ordered sequence of items.  
continents = ('Asia', 'Africa', 'Americas', 'Europe', 'Australia')
print(continents)


# Difference
# The only difference between it and a list is that a tuple is immutable. 
# This means that once it has been created, it cannot be modified.

# update List
weekdays[0] = 'Updated'
print(weekdays) #List value updated 

# update Tuple
continents[0] = 'Updated' 
# it will give (TypeError: 'tuple' object does not support item assignment)
print(continents)

# However It is possible add another Tuple
continents2 = ('Antarctica',)
all_continents = continents + continents2
print (all_continents)

# Also it is possible delete a Tuple
print (continents2)
del continents2
print (continents2) # It is no longer available (NameError: name 'continents2' is not defined)


"""
Reference

Radha Chawla. (2021). PROG8420_Week 4_CollectionObjectType slide 21 [PowerPoint slides]. eConestoga.

Radha Chawla. (2021). PROG8420_Week 5_W5 - 1 - CollectionObjectType slide 18 [PowerPoint slides]. eConestoga.

"""

"""
-------------------------------------------------------------------------------
Question 5: What is __name__ in python and its purpose? [2 Marks]
-------------------------------------------------------------------------------
"""
"""
Answer: __name__

The __name__ variable (two underscores before and after) is a special Python variable.
In Python, we can import that script as a module in another script.

If the file is executed as the main program, the interpreter sets the __name__ 
variable value to “__main__”. Else if this file is being imported from another
module, __name__ will be set to the module’s name.
"""
# Example
# Write following code in a file name mod1.py

def M1_F1(x):
    print('From mod1 file we see namespace...', __name__)
    print('The passed value is', x)
    
# Write following code in another file name say main.py
    
import mod1
    
print('From main file we see namespace...', __name__)
mod1.M1_F1('Hasan Mahamud Rana')


"""
Reference

Radha Chawla. (2021). PROG8420_Week 3_Week 3 - 1 slide 3 [PowerPoint slides]. eConestoga.
Python 3.9.5 Documentation, (August, 2012) 
The Import system https://docs.python.org/3/reference/import.html?highlight=__name#__name__

"""
"""
-------------------------------------------------------------------------------
Question 6: Write a program that prompts user to enter a number and then prints
the number of coins of each type required to make the given amount of change. [5 marks]
-------------------------------------------------------------------------------
"""

def amountOfChange(amount):

    if amount <= 0:
        print('no change')
    else:
        d = int(amount)
        c = valueAfterDecimal(amount)
           
        return {'dollars': dollars(d), 'cents': cents(c)} 

def valueAfterDecimal(amount):    
    return int(str(amount).split('.')[-1][:2])

def dollars(d):
    dollar_100 = d // 100
    d %= 100
    
    dollar_50 = d // 50
    d %= 50
    
    dollar_20 = d // 20
    d %= 20
    
    dollar_10 = d // 10
    d %= 10
   
    dollar_5 = d // 5
    d %= 5
    
    dollar_1 = d
        
    return {
        '$100': dollar_100,
        '$50': dollar_50, 
        '$20': dollar_20, 
        '$10': dollar_10,
        '$5': dollar_5, 
        '$1': dollar_1
    }

def cents(c):
    num_quarters = c // 25
    c %= 25
    
    num_dimes = c // 10
    c %= 10
    
    num_nickles = c // 5
    c %= 5
    
    num_pennies = c
    
    return { 
        'quarters': num_quarters,
        'dimes': num_dimes,
        'nickels': num_nickles,
        'pennies': num_pennies,
    }

amount = float(input('Enter your amount: '))
result = amountOfChange(amount)

for i in result:
    print('\n{}'.format(i.upper()))
    for j in result[i]:
        print(result[i][j], j)

"""
Reference

Radha Chawla. (2021). PROG8420_W6 - 01 - Loops slide 7 [PowerPoint slides]. eConestoga.

"""
"""
_______________________________________________________________________________

Question 7: Write a program to get three inputs from user and compare these 
three numbers. [4 marks]
_______________________________________________________________________________
"""

#Simplest version
number1 = int(input('Enter First number: '))
number2 = int(input('Enter Second number: '))
number3 = int(input('Enter Third number: '))

def compare(numbers):
    # get min value from list
    print('\nThe smallest of the 3 numbers is: {}'.format(min(numbers))) 
    
    # get mid value from list
    numbers.sort()
    print('The mid value of the 3 numbers is: {}'.format(numbers[int(len(numbers)/2)]))  
    
    # get max value from list
    print('The largest of the 3 numbers is: {}'.format(max(numbers)))  

#creating a list from user input    
numbers = [number1, number2, number3] 
compare(numbers)


"""
Reference

Radha Chawla. (2021). PROG8420_Week 5 - 1 - CollectionObjectType slide 5 [PowerPoint slides]. eConestoga.

"""


"""
_______________________________________________________________________________

Question 8: Create an example of nested list, dictionaries and extract the value
from inner most index.[2 marks]
_______________________________________________________________________________
"""

# Declare nested list
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff', ['gggg', 'hhhhh']]], 'i', 'j']

# Read inner most index
print('Read inner most index from list:', L[2][2][2][0])


# Reclare nested dictionaries
rec = {
    'name': {
        'fname':'Hasan', 
        'lname': 'Rana'
        },
    'job': ['dev', 'manager', 'cricketer'],
    'age': 35,
    'hits': {
        'index': '6307359707',
        'type': 'IngredientsType',
        'id': '2',
        'score': 1,
        'source': {
            'MainItemNo': '200111',
            'LineNo': '20000',
            'Description': 'Test Ingredient',
            'CategoryCode': 'Test'
            }
        }
    }

# Read dictionaries
print('Read inner most index from dictionaries:',rec['hits']['source']['MainItemNo'])
print('Read inner most index from dictionaries:',rec['hits']['source']['Description'])
 

"""
Reference

Radha Chawla. (2021). PROG8420_Week 5 - 1 - CollectionObjectType slide 3, 11 [PowerPoint slides]. eConestoga.

"""

"""
_______________________________________________________________________________

Question 9: Is python an interpreted language. If yes, why if not explain. [2 marks]
_______________________________________________________________________________
"""

# Python is considered an interpreted language because Python programs are executed by an interpreter.
# Interpreter - processes the program a little at a time, line by line.
# SOURCE CODE -> INTERPRETER -> OUTPUT 


"""
Reference

Radha Chawla. (2021). PROG8420_Week 2 - 1, slide 3,4 [PowerPoint slides]. eConestoga.

"""