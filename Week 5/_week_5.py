# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:07:49 2021

@author: Hasan Mahamud Rana
"""

#Nested list
m =[[1,2,3],[4,5,6],[7,8,9]]

m
m[1]
m[1][1]


#multi list

m1 = [1,2,3,4]
m2 = [1,2,3,m1]
m3 = [1,2,3,m2]

m3

m3[3]
m3[3][3]
m3[3][3][0]

#list comprehension Expresion

diag = [m[i][i] for i in [0,1,2]] #diagonal of list
diag

twice = [c*2 for c in 'Spam']
twice

twice.count('pp')

d = {'fname':'Hasan', 'lname': 'Rana', 'qty': 4, 'color':'blue'}
d

d['fname']
d['qty']
d['color']

d['qty'] = 9
d

d1= {}
d1['fname'] = 'Rana'
d1['age'] = 35 
d1['job'] = 'dev'

d1

print(d1['fname'])

#Dctionary manipulation
rec = {
       'name': {'fname':'Hasan', 'lname': 'Rana'},
       'job': ['dev', 'manager'],
       'age': 35
      }

print(rec['name'])
print(rec['name']['fname'])
print(rec['name']['lname'])

print(rec['job'])
print(rec['job'][0])
print(rec['job'][-1])
print(rec['age'])

rec['job'].append('cricketer')
rec


d2 = {'a': 1,'b': 2,'c': 3}
d2


ks = list(d2.keys())
ks

ks[0] = 'd'
ks

v = d2.values()
v

ks.sort()

for key in ks:
        print (key, '=>', d2[key])


for c in 'spam':
    print(c.upper())
    

x =4
while x > 0:
    print('Spam!' * x)
    x -= 1    


if not 'f' in d2:
    print('Missing')

v2 = d2.get('x', 0)
v2
v2 = d2['x'] if 'x' in d2 else 0
v2

#------------------------------------------------
#Tuples

T = (1,2,3,4)
len(T)

T + (5,6)

T[0]


continents = ('Asia','Africa','America','Europe','Australia')


#Accessing tupples
print('continents[0]:', continents[0])
print('continents[2:]:', continents[2:])
print('continents[:-3]:', continents[:-3])

#Updating tupples
continents2 = ('Antarctica',)
continents2

all_continents = continents + continents2
print(all_continents)


#deleting
del continents2
continents2

all_continents = continents + continents2
print(all_continents)











