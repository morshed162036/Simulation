# -*- coding: utf-8 -*-
"""Tausworthe generation technique

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zBf4XwA4VZyhar-mNuHkrqL0ICS4oHF8
"""

import numpy as np
l=4
N=100*l
r=3
q=5
b_i=[1,1,1,1,1]
for i in range(5,N):
    b = ((b_i[i-r]) + (b_i[i-q]) ) %2
    b_i.append(b)
    #print(b) 
    #print(b_i)
    
a=2**l
val=[]
u = []
for i in range(0,N,l):
  bit_segment=b_i[i:i+l]
  #print(bit_segment)
  str1=""
  for j in bit_segment:
    str1=str1+str(j)
  #print(str1)
  value= int(str1,2)
  u.append(value/a)
  val.append(value)

print(val)
print(u)

import numpy as np
l=4
N=1000*l
r=3
q=5
b_i=[1,1,1,1,1]
for i in range(5,N):
    b = ((b_i[i-r]) + (b_i[i-q]) ) %2
    b_i.append(b)
    #print(b) 
    #print(b_i)
    
a=2**l
val=[]
u = []
for i in range(0,N,l):
  bit_segment=b_i[i:i+l]
  #print(bit_segment)
  str1=""
  for j in bit_segment:
    str1=str1+str(j)
  #print(str1)
  value= int(str1,2)
  u.append(value/a)
  val.append(value)

print(val)
print(u)

import numpy as np
l=4
N=5000*l
r=3
q=5
b_i=[1,1,1,1,1]
for i in range(5,N):
    b = ((b_i[i-r]) + (b_i[i-q]) ) %2
    b_i.append(b)
    #print(b) 
    #print(b_i)
    
a=2**l
val=[]
u = []
for i in range(0,N,l):
  bit_segment=b_i[i:i+l]
  #print(bit_segment)
  str1=""
  for j in bit_segment:
    str1=str1+str(j)
  #print(str1)
  value= int(str1,2)
  u.append(value/a)
  val.append(value)

print(val)
print(u)  
#print(len(u))

from matplotlib import pyplot as plt
plt.bar(range(len(u)),u)
plt.xlabel('index of random number, i')
plt.ylabel('the random number U')
plt.show()