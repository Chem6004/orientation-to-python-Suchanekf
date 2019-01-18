# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:40:14 2019

@author: suchanekf
"""

 #print("Hello World!")
 ### variables for particle 1 
import numpy as np
Npart = 10

### create empty lists for each quantity
m = np.zeros(Npart)
v = np.zeros(Npart)
q = np.zeros(Npart)
x = np.zeros(Npart) 
T = np.zeros(Npart)
###print the array of zeros for m
print(m)

for i in range (0,Npart):
    m[i] = 1.0
    q[i] = 1.0
    x[i] = 0.5 * i
    v[i] = 0.2 * i

    ### now that I have mass and velocity got the 
    ### ith particle, I can calculate kinetic energy
    ### for the ith particle
    T[i] = 0.5 * m[i] * v[i]**2

print(T)

print (m)
print (q)
print (x)
print (v)
### variables for pair of particles
r12 = np.sqrt((x1-x2)**2)
v12 = q1*q2/r12
print(" separation is ", r12)
print("Potential Energy is ",v12)


