# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class NewClass:
    name = str(input('Enter you name: '))
    def greeting(name):
            print("Hello", name)
            
myObject = NewClass()
print(NewClass.name)
print(NewClass.greeting)
print(myObject.greeting)

myObject.greeting()

class  myClass():
    def setName(self, name):
        self.name=name
    def setAge(self, age):
        self.age=age    
        
   
        
Me = myClass()
Me.setName('Nigar Sultana')       
Me.setAge(27)  
print(Me.name)
print(Me.age)  