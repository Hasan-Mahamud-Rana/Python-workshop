# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:25:32 2021

@author: 16476
"""

def checkInput(prompt):
  result = None
  while result == None:
    try:
      result = input(prompt)
      return result
    except:
      print("Please insert an appropriate value!")