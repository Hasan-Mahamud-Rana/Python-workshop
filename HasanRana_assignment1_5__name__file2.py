# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:44:06 2021

@author: Hasan Mahamud Rana

Question 5: What is __name__ in python and its purpose? [2 marks]

"""

# File2.py 
  
import HasanRana_assignment1_5__name__file1 
  
print ("File2 __name__ = %s" %__name__) 
  
if __name__ == "__main__": 
    print ("File2 is being run directly")
else: 
    print ("File2 is being imported")


