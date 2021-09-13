# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 22:07:18 2021

@author: Hasan Mahamud Rana
"""

# Take-home Activity
# Write a program that prompts the user for a string and places the string in a list.
# When the user types “end” the program prints out the list – one entry per line – and stops

userList = []

#method 1, add item to the list using "append"
while True:
    
    el = input('Enter the element: ')
    userList.append(el)
    
    end = input('Type "end" to stop and print your list: ')
    if end == 'end':
        break

#method 2, add item to the list using "insert"
while True:
    
    el = input('Enter the element: ')
    userList.insert(len(userList), el)
    
    end = input('Type "end" to stop and print your list: ')
    if end == 'end':
        break

#method 3, break in the same input
while True:
    
    el = input('Enter element or type "end" to stop and print your list: ')
    
    if el != 'end':
        userList.append(el)
    else:  
        break


#method 1, print list one entry per line
print('Here is your list:')
print('\n'.join(map(str, userList)))

#method 2, print list one entry per line
print('\nHere is your list:', *userList, sep = '\n')