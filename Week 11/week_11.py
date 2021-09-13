# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:29:01 2021

@author: 16476
"""

class Point:
    """This is point class"""
    
class Rect:
    """This is react clsss with 3 attributes length, width, corner"""

    def move_rectangle(self, r, dx, dy):
        r.corner.x += dx
        r.corner.y += dy
        
        
p = Point()

p.x = 5
p.y = 10
print(p.x, ' ', p.y);        


React_1 = Point()

React_1.length = 10
React_1.width = 5
print(React_1.length, ' ', React_1.width);    


React_1.corner = Point()

React_1.corner.x = 2
React_1.corner.y = 4
print(React_1.corner.x, ' ', React_1.corner.y); 


React_1.move_rectangle(React_1, 10, 10)




class c1():
    def ___init__(self):
        return

x = c1()    
x



class Employee:
    def ___init__(self, name):
        self.surname=input()
        self.firstname=name
    
        def Name(self):
            print(self.firstname)
            print(self.surname)
        
y = Employee()


import math

class GeoObj():
    def __init__(self,color="red",filled=True):
        self._color=color
        self._filled=filled
            
    def get_color(self):
        return self._color
    
    def set_color(self,color): 
        self._color=color
        
    def is_filled(self):
        return self._filled
    
    def set_filled(self,filled):
        self._filled=filled
        
        
class Circle(GeoObj):
    """ Circle class inheriting GeoObj"""
    def __init__(self,radius=10,color="red",filled=True):
       super().__init__(color,filled)
       self._radius=radius
    
    def get_radius(self):
       return self._radius
    
    def set_radius(self,radius):
       self._radius=radius
    
    def get_area(self):
       return math.pi*self._radius**2
    
    def get_perimeter(self):
       return 2*math.pi*self._radius
    
    def get_diameter(self):
       return 2*self._radius
    
    def print(self):
       if self.is_filled():
           fill =" filled"
       else:
           fill="not filled"
       print("This is ", fill, self.get_color(),"circle")
    
    def __str__(self):
       if self.is_filled():
           fill =" filled"
       else:
           fill="not filled"
           
       return "Circle "+ fill+"," +self.get_color()+", radius :" +str(self._radius)+"."
           
           

