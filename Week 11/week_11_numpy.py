# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:54:48 2021

@author: Hasan Mahamud Rana
"""

import numpy as np


print(dir(np))

a1_list = [1,2,3,4,5,6]
a_array = np.array(a1_list)
print(a_array)


a_multi_list = [[1,2,3],[4,5,6]]
multi_array = np.array(a_multi_list)
print(multi_array)

#finding array shape
print(multi_array.shape)


print(a_array[2])

print(multi_array[0][2])

a = np.zeros((2,3))
print(a)

a = np.ones((2,3))
print(a)


a = np.full((2,3),5)
print(a)

a = np.eye(5)
print(a)

a = np.random.random((3,4))
print(a)


a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
a = np.array(a)
print(a)

b = a[0:3, 1:3]
print(b)

b = a[1:, 1:]
print(b)




from getpass import getpass
import smtplib

 

s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()

 

email = "imagine.blackpearl@gmail.com"
password = getpass()
s.login(user=email, password=password)

 

receiver_email = "rana_imagine@yahoo.com"
subject = "Test Email"
body = "This is a test email for testing email functionality for python project."
combined_msg = f"From:{email}\nTo:{receiver_email}\nSubject:{subject}\n{body}"

 

# Send the email.

 

s.sendmail(from_addr=email, to_addrs=receiver_email, msg=combined_msg)
s.close()






