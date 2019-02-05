
### variables for particle i 
import numpy as np
Npart = 20
print(Npart)
### create empty lists for each quantity
m = np.zeros(Npart)
v = np.zeros(Npart) 
T = np.zeros(Npart)
###print the array of zeros for m
for i in range (0,Npart):
    m[i] = 1.0
    v[i] = 3.5  
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
print("Kinetic energy is for each particule", T)

