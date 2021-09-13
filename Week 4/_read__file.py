# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:24:10 2021

@author: Hasan Mahamud Rana
"""

f = open('data.txt', 'w')
f.write('hello\n')
f.write('world\n')
f.close()


f = open('data.txt')
text = f.read()
text
print(text)

text.split()

X= set('spam')
Y= {'h','a','m'}

X,Y
X&Y
X|Y
X-Y

{x**2 for x in [1,2,3,4]}

f = open('data.txt')
lines = f.readlines()

type(lines)


if type(lines) == type([]):
    print('yes')
    
if type(lines) == list:
    print('yes')
    
if isinstance(lines, list):
    print('yes')
    
    
    
    
    
    
    
input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
# print list
print('list: ', user_list)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

# Calculating the sum of list elements
print("Sum = ", sum(user_list))












#--------------------------------

number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)

#--------------------------------

choice = 'eggs'

if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bcon':
    print(1.10)
else:
    print('Bad')    


#----------------------------------
input_string = input("Enter all family members name separated by space  ")
# Split string into words
family_list = input_string.split(" ")

print("\n")
# Iterate a list
print("Printing all family member names")
for name in family_list:
    print(name)

#----------------------------------

 
choice = 'Monday'
day_week={'day1':'Monday', 'day2':'Tuesday'}

print(day_week['day1'])
print(day_week.get('day1', 'Wrong'))

'day1' in day_week

#----------------------------------

try:
    print(day_week['day1'])

Except:
    print('Not valid key')
    
    
x=1
if x:
    y=2
    if y == 1:
        print('1')
    print('2')
print('3')
    

x='spam'
if 'rubbery' in 'shrubbery':
    print(x*8)
    x+='NI'
    if x.endswith('NI'):
        x*=2
    print(x)

    
    