# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:44:02 2021

@author: Imagine
"""

text="My name is {name}, i'm a {role}".format(name="rana", role="WEB developer")

print(text)

text

type(text)






x = 2
print(x, type(x))

y = 2.0
print(y, type(y))


z = 1+2j
print(z, type(z))

isinstance(1+2j, complex)
isinstance(z, complex)
isinstance(z, float)



v1  = '123'

v2 = int(v1)+2
v2

v3 = str(v2)
type(v2)

type(v3)


name = input('Who m i talking to..')
print('Hi ', name)

inp = input('EU floor number ')
usf = int(inp) + 1
print('Canada floor', usf)


hour = input('How many hours ')
rate = input('Hourly rate ')
pay = float(hour) * float(rate)
print('Total', pay)



import math
math.pi
math.sqrt(12)

import random
random.random()

random.choice([1,2,3,4])

dir(math)

from inspect import getmembers
getmembers('math')

x=2
y=4

pow(x,y)
math.pow(x, y)
