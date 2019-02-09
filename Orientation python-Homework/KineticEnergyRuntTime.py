#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
Npart = 30
### 1-D arrays of length Npart for q... assign each particle charge of 1 natural unit
q = np.ones(Npart)

### create a 1-D array of length Npart for x... use np.linspace to automatically
### assign values since we want the particles evenly spaced.
x = np.linspace(0,(Npart-1)*0.2,Npart)

### create a 2-D array that is Npart x Npart for the separations between particle pairs
r = np.zeros((Npart,Npart))

### compute all separations using two nested for-loops to access the positions of each particle
for i in range(0,Npart):
    for j in range(0,Npart):
        r[i][j] = np.sqrt( (x[i]-x[j])**2 )

### now print all arrays 
print("Printing array of charges ",q)
print("Printing array of charges ",x)
print("Printing array of charges \n",r)
## function to compute potential energy given an array of separations and an array of charges
def Potential(sep_array, charge_array):
    ### presumably the number of particles is equal to the length
    ### of the array of charges
    N = len(charge_array)
    
    ### initialize the potential energy to zer
    Pot = 0.
    ### nested loop
    for i in range(0,N):
        for j in range(0,N):
            ### do not calculate potential of particle with itself!
            if (i!=j):
                Pot = Pot + charge_array[i]*charge_array[j]/sep_array[i][j]
    return Pot
### Compute total potential energy and store it as the variable V_tot
V_tot = Potential(r, q)

### print it to see what it is!
print(V_tot)
### import time library
import time
### import pyplot as library
from matplotlib import pyplot as plt

### get the time at the beginning of the program
start = time.time()
### create an array of 100 x-values between -5 and 5
x = np.linspace(-5,6,100)
### create an array of y-values defined as y = x^2
y = x**2

### plot y = x^2 with a red line!
plt.plot(x, y, 'red')
plt.xlim(0,6)
plt.ylim(0,36)
plt.show()

### figure out how much time this whole program took to run!
end = time.time()
how_long = end - start
### print the total time taken in seconds
print(" Total time to run in seconds is: ",how_long)

