#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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



print("Kinetic energy is ", T)

print (m)
print (q)
print (x)
print (v)
### variables for pair of particles
r12 = np.sqrt((x[1]-x[2])**2)
v12 = q[1]*q[2]/r12
print("Separation is ", r12)
print("Potential Energy is ",v12)
