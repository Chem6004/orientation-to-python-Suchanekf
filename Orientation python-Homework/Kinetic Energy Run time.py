#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 #print("Hello World!")
 ### variables for particle 1 
import numpy as np
Npart = 35
print(Npart)
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
    ### initialize a sum variable to zero
T_tot_loop = 0.
### loop over elements of the T array and 
### compute the sum 
for i in range(0,Npart):
    ### add elements to the sum variable
    T_tot_loop = T_tot_loop + T[i]
    
### compute the sum using np.sum instead
T_tot_sum = np.sum(T)

### print both sums to confirm both methods give the same answer
print("Result from loop is ",T_tot_loop)
print("Result from numpy sum is ",T_tot_sum)
print("Kinetic energy is ", T)
### import time library
import time
### import pyplot as library
from matplotlib import pyplot as plt
### get the time at the beginning of the program
start = time.time()
### create an array of 100 x-values between -5 and 5
x = np.linspace(-5,30,100)
### create an array of y-values defined as y = x^2
y = x**2

### plot y = x^2 with a red line!
plt.plot(x, y, 'red')
plt.xlim(0,40)
plt.ylim(0,1600)
plt.show()
### figure out how much time this whole program took to run!
end = time.time()
how_long = end - start
### print the total time taken in seconds
print(" Total time to run in seconds is: ",how_long)

