# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:07:49 2021

@author: Hasan Mahamud Rana
"""
 
numbers = [3,6,9,2,5,8,1,4,7]
sum = 0
for val in numbers:
    sum += val
    print('The sum so far', sum)
    
    
total = 0
for x in range(10,20,2):
    total += x
    print('The total so far', total)
    
    
for i in numbers:
    print(i)
else:
    print('Done, no more to print')    
    
    
for n in range(2, 10):
    for x in range(2, n):
        if n% x == 0:
            print(n, 'equal', x, '*', n/x)
            break
    else:
        print(n, 'Is prime number')
        
        


a_string = "Hasan Mahamud Rana"
lowercase = a_string.lower()

vowel_counts = {}

for vowel in "aeiou":
    count = lowercase.count(vowel)

    vowel_counts[vowel] = count

print(vowel_counts)



n = 5

while n > 0:
    print(n)
    n=n-1
    
print('Done')



n = 5

while n != 0:
    print(n)
    n -= 1
else:    
    print('Done')
    
    
while True:
    line = input('Enter a word: ')  
    if line == 'done':
        break
    print(line)

print('Done!')    


A,B,C,D=1,2,3,4

X = (A+B+
     B+D)

if(A==1 and
   B==2 and
   C==3) :
    print('Hello' *3)
    
while True:
    reply = input('Enter a value: ')  
    if reply == 'stop':
        break
        print(int(reply) ** 2)    
    print('Go again!')  
    

while True:
    reply = input('Enter a value: ')  
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' *  2)
    else:
        print(int(reply) ** 2)    
        print('Next.. \n')   


while True:
    reply = input('Enter a text: ')  
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Bad!' *  4)
    else:
        print(int(reply) ** 2)    
        print('Bye') 
        