# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:27:15 2021

@author: Imagine
"""



print('Hello, Welcome to python Class!', end='Rana')
print('Bye.')

import script1

from imp import reload
reload(script1)


import myfile
print(myfile.title)


from myfile import title
print(title)


import threenames
threenames.b, threenames.c


from threenames import a,b,c
b,c

dir(threenames)
 
