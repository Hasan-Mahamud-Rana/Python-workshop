# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:24:10 2021

@author: Imagine
"""

def PrimeOrNot(num):
    # define a flag variable
    flag = False
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    
    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


def prime_number(x):
    # prime numbers are greater than 1
    if(x>1):
         # check for factors
        for i in range(2, x):
            if (x % i == 0):
                print(x, 'Not a prime number')
        else:
            print(x, 'Prime number')
            
    else:
        print(x, 'not a prime number')

         
num = int(input("Enter a number: "))
PrimeOrNot(num)
prime_number(num)
 