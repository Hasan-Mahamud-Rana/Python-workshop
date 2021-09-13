# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:07:49 2021

@author: Hasan Mahamud Rana
"""

import re

txt1 = 'Today, it is raining in Spain'
x1 = re.findall('ai ', txt1)

print(x1)


txt2 = 'Today, it is raining in Spain'
x2 = re.findall('', txt2)

print(x2)


txt3 = 'Today, it is raining in Spain'
x3 = re.findall('12', txt3)

print(x3)


txt4 = 'The cat sat on the mat'
x4 = re.search('1', txt4)

print('The first white-sapce character is located in position:', x4)


txt5 = "Ding dong bell"
x5 = re.search('on', txt5)

print(x5.span())
print(x5.group())
print(x5.string)


txt6 = 'The cat sat on the mat'
x6 = re.split('\s', txt6)
print(x6)

x6 = re.split('\s', txt6, 1)
print(x6)

x6 = re.split('\s', txt6, 2)
print(x6)


x6 = re.split('\s', txt6, 3)
print(x6)

x6 = re.split('\s', txt6, -1)
print(x6)

txt7 = 'The cat sat on the mat'
x7 = re.sub('\s', 9, txt7)
print(x7)


line = 'The cat sat on the mat'
reg_match = re.match('(.*) on (.*)', line)
print(reg_match)
print(reg_match.group())
print(reg_match.group(1))
print(reg_match.group(2))


reg_match = re.match('on', line)


txt8 = 'www.mysite.com then blah blah and finally ftp.example.com blah'

re = txt8.compile('a/{1,3}b+')


list = 'a111 222 111 114 11 a11441b'
text = re.compile('a\d{3}')
print(text.findall(list))


list = '111 222 111 114 11 aab abbb abb a///b a///bb a/b ///66fjvj bbbb aaab'
res = re.findall('[0-9]+ | [a-z]+', list)

print(list)

print(re.search('}s' '{block}'))
print(re.search('}s' '{block} '))
print(re.search('}s' '{block}\n'))


p = re.compile(r'\bclass\b')
print (p.search('no class at all'))

print (p.search('The declassified algorithm'))