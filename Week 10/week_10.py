# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

print(re.search('}$', '{block}'))
print(re.search('}$', '{block} '))
print(re.search('}$', '{block}\n'))


p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))

list = '''aaab abdcabdc abcabcd abc abccc abbbc'''
res = re.search('(abc){2,3}', list)
print(res)

txt = "The cat sat on the mat"
x = re.search('^The.*mat$', txt)
print(x)


txt1 = "The cat sat on the red mat. #this is a comment"
y = re.sub('(#.*)','', txt1)
print(y)


txt2 = "The 'cat-', sat on the  'red -mat' .#This is a comment"
x = re.sub 

list1 = "cat, sat, beat, bat, eat"
my_match = re.compile('[cbe]at')
list2 = my_match.findall(list1)

print(list2)





def print_sentence(print_sentence):

    my_match = re.compile('[ch][a-z]*')
    list2 = my_match.findall(print_sentence)

    print(list2)
     

         
sentence = input("Write your sentence: ")
print_sentence(sentence)
 








