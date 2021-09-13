# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:19:08 2021

@author: Hasan Mahamud Rana
"""
# function 

def exp(x,y):
    z = x ** y
    return z


x = 2
y = 4

result = exp(x,y)
result


def foo():
    pass

dir(foo)

foo.score = 10

print(foo.score)


def zero(s1, s2):
    print('start value s1',s1)
    print('start value s2',s2)
    s1=[1,2,3]
    s2=[4,5,6]
    print('end value s1',s1)
    print('end value s2',s2)
    return(s1,s2)

s1='spam'
s2={1:'a', 2:'b', 3:'c'}

s3 = zero(s1, s2)

print(s1)
print(s2)
print(s3[0])
print(s3[1]) 




#program 1
def absoluteNumber(n):
    print("The absolute value of an integer number is:", abs(n))
 
n = int(input("Enter a number: "))    
absoluteNumber(n)
   
def absoluteNumber2(m):
    if m < 0:
        print("The absolute value of an integer number is:", (m * -1))
    else:
        print("The absolute value of an integer number is:", m)
 
m = int(input("Enter a number: "))    
absoluteNumber2(m)   


#program 2
def evenOdd(num):
    if (num % 2) == 0:
       print("{0} is Even number".format(num))
    else:
       print("{0} is Odd number".format(num))


num = int(input("Enter a number: "))
evenOdd(num)


#program 3
def summation(x,y):
    z = x + y
    return z

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = summation(x,y)
print("Result: ",  result)



def fun(x=5,y=2,z=3):
    return (x+y-z)

fun()
fun(3)
fun(4, 2)


def concatString(a,b):
    strType = type('')
    if type(a) == strType and type(b) == strType:
        return(a+' '+b)
    
print('String', concatString('Hasan', 'Rana')) 
print('Number', concatString(5, 4)) 


def mult(i,j):
    return(i*j)

mult(3,4)
mult('spam', 4)



def intersect(seq1, seq2):
    res = []
    for x in seq1:
        for x in seq2:
            res.append(x)
    return(res)

intersect('Hasan','Rana')


def foo2(a, b, c=4, *arg, **karg):
    return a, b, c, arg, karg

foo2(1, 2)
foo2(1, 2, 3, 4, 5)
foo2(1, 2, 3, 4, 5, 9, d=6, e=7, g=8)




