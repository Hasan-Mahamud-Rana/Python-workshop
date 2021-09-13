# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:58:28 2021

@author: Hasan Mahamud Rana
"""

F = open('_prime__number.py', 'r')

#------------------------------------------------------------------------------
#Excercise
#Print full file using read()
print(F.read())

#Print how many characters you want to return
print(F.read(150))

#Print file using loop
for l in F:
  print(l)
  
#HOME ACTIVITY
#Write a program to open a file and print each line in the program
#to screen prefixed by the line number

#------------------------------------------------------------------------------
#Method 1
#Get all lines at once using readlines(), lines data type is List
lines = F.readlines()

i = 0
for line in lines:
    if line.strip() != '':
        i += 1
        # Strips the newline character
        print('m1.{}: {}'.format(i, line.strip())) 




#------------------------------------------------------------------------------
#Method 2    
#Using readline()    

j = 0
while True:
    j += 1
 
    # Get next line from file, one line at a time
    line = F.readline()
 
    # if line is empty and end of file is reached
    if not line:
        break
    print('m2.{}: {}'.format(j, line.rstrip()))
    
    
    
#------------------------------------------------------------------------------
#Method 3
with F as f:
    #Use enumerate(f, start=1) to avoid the addition.
    for k, line in enumerate(f, start=1):
        print('m3.{} = {}'.format(k, line.rstrip()))    
