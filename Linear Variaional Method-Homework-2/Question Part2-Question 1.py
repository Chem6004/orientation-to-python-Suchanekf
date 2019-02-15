#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
def H_ij(i,j):
    a = 0
    b = ((np.pi**2)*(j**2)/200)Matri
    
    ham_int = a+b
    
    if i==j:
        ham_int = a+b

    else:
        ham_int = a
        
    return ham_int

H_mat = np.zeros((3,3))

for i in range (1,4):
    for j in range (1,4):
        H_mat[i-1][j-1] = H_ij(i,j)

print(H_mat)

### create an empty numpy array for the c vector
c = np.zeros(3)
### assign c vector to be (1, 0, 0)
c[0] = 1
c[0] = 0
c[1] = 0

### compute H_mat * c and store it to a new array called Hc
Hc = np.dot(H_mat,c)

### compute c^t * Hc and store it to a variable E
E = np.dot(np.transpose(c),Hc)

### print the result
print(E)
### compute eigenvalues and eigenvectors of H_mat
### store eigenvalues to E_opt and eigenvectors to c_opt
E_opt, c_opt = np.linalg.eig(H_mat)

### print lowest eigenvalues corresponding to the 
### variational estimate of the ground state energy
print(E_opt[0])

### print coefficients that define the trial wavefunction with the lowest eigenvalue
### which corresponds to the variational estimate of the ground state wavefunction
print(c_opt[0])


