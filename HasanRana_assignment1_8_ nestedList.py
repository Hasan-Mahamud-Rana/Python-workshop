# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:44:06 2021

@author: Hasan Mahamud Rana

Question 8: Create an example of nested list, dictionaries and extract the value
from inner most index.[2 marks]

 
"""
# declare list
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(L[2])
print(L[2][2])
print(L[2][2][0])


# declare dictionaries
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# read dictionaries
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])