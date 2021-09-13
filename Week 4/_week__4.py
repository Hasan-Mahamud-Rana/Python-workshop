# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:19:13 2021

@author: Hasan Mahamud Rana
"""

s='123'
pie = '3.14'

x =int(s) +1
x

y = float(pie) +1
y

z_bad = int(s) + int(pie)
z_bad

z_good = int(s) + int(float(pie))
z_good


S = 'Spam'
len(S)
S[0]
S[1]
S[-1]
S[len(S)-1]


S[0:2]
S[2:]
S[0:3]
S[:2]
S[:-1]
S[:]


S + 'abc'
S*8


S


S.find('pa')

S.find('cd')



t = 'Hasan Mamamud Rana'

t.find('a')

t.replace('a', 'A')

t.isalpha()

line ='aaa,bbb,ccc,ddd'
line = line.rstrip('b')
line = line.split(',')

type(line)

email = 'e@y.com'
email = email.split('@')

email[0]
email[1]


for word in email:
    print(email)
    print(word)



original_string = "e@gmail.com"
characters_to_remove = "@."

new_string = original_string
for character in characters_to_remove:
  new_string = new_string.replace(character, "")

print(new_string)

tt = 'papaya'
tt.replace('pa','za')

name = 'HASAN'
o = "Pyhton Programmer"
c = """TEST comment"""

print(name)
print(o)
print(c)

w, x,y,z = 10,15,20,25

print(w, x,y,z)

print(w, x,y,z, sep=',')
print(w, x,y,z, sep='')
print(w, x,y,z, sep=':')
print(w, x,y,z, sep='---')


S= 'A\nB\tC'
len(S)


weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

print(weekdays)

type(weekdays)

yearlist = [2017, "two thousand seventen", "XXVII", 20.17]

type(yearlist)

fav = ["a", "x","i", "ss"]
fav

months=['Jan','Feb', 'Mar', 'Apr', 'May','Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months[0]
months[4:9]
months[-2]
months[6:]

L = [1,2,3]
L = L + [4,5,6]
L


sub = ['mayh', 'physics', 'chemistry']
sub

sub[2] = 'biology'
sub

sub.append('bangla')
sub

del sub[2]
sub

sub.remove('bangla')
sub

M = ['bb','cc', 'aa']
M.sort()
M

M.reverse()
M


N = M + [1,2,3]
N
N.sort()
N
N.reverse()
N
