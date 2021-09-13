# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:44:06 2021

@author: Hasan Mahamud Rana

Question 6: Write a program that prompts user to enter a number and then prints
the number of coins of each type required to make the given amount of change. [5 marks]
 
"""

def change(n):

    if n <= 0:
    
        print('no change')
    
    else:
        
        d = int(n)
        c = valueAfterDecimal(n)
           
        return dollars(d), cents(c)

def valueAfterDecimal(n):    
    return int(str(n).split('.')[-1])


def dollars(d):
    dollar_50 = d // 50
    d %= 50
    
    dollar_20 = d // 20
    d %= 20
    
    dollar_10 = d // 10
    d %= 10
   
    dollar_5 = d // 5
    d %= 5
    
    dollar_1 = d
    
    return dollar_50, dollar_20, dollar_10, dollar_5, dollar_1

def cents(c):
    num_quarters = c // 25
    c %= 25
    
    num_dimes = c // 10
    c %= 10
    
    num_nickles = c // 5
    c %= 5
    
    num_pennies = c
    
    return num_quarters, num_dimes, num_nickles, num_pennies

n = float(input('Enter CAD: '))
result = change(n)

print('{} $50, {} $20, {} $10, {} $5, {} $1'.format(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4]))
print('{} quarters, {} dimes, {} nickels, {} pennies'.format(result[1][0], result[1][1], result[1][2], result[1][3]))




