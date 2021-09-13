# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:22:09 2021

@author: Hasan Mahamud Rana

Question 3: Write a program to check odd or even number.[5marks]

"""

#Even Odd Program using Modulus Operator  
 
a = int(input("Please Enter a Number : "));  

if (a%2 == 0):  
    print("This Number is Even")  
else:  
    print("This Number is Odd")  


#Even Odd Program using Bitwise Operator  
a = int(input("Please Enter a Number : "));  

if(a&1 == 1):  
    print("This Number is Odd")    
else:  
    print("This Number is Even")   


#Even Odd Program using Modulus Operator  

number=int(input("Please Enter a Number : "));  
x=int(number/2)*2;  
x

if(x==number):  
    print("This Number is Even")    
else:  
    print("This Number is Odd")  