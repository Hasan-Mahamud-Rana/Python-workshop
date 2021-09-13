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

Question 1: Write a python program to display the multiplication table with 
taking input from the user. [5 marks]

"""

import HasanRana_assignment1_0_checkInput

Num = input("Enter the Number :")
ValidatedNum = HasanRana_assignment1_0_checkInput.checkInput(Num)
ValidatedNum = int(ValidatedNum) if ValidatedNum else 0

for i in range(1,11) :
    print(ValidatedNum, "X", i, "=", ValidatedNum*i)
    

number = int(input('enter number:'))
limit = int(input('enetr limit:'))
limit = 10 if limit == 0 else limit
limit

for mul in range(1,limit+1):
    result = number * mul
    print('{} * {} = {}'.format(number, mul, result))

    
try:
    y = input('Number>>')
except SyntaxError:
    y = None
    
y
    


name = input("What is your name? ") 
HasanRana_assignment1_0_checkInput.checkInput(name)

print("Hello, %s." % name)  
print("Hello, {}.".format(name))  

