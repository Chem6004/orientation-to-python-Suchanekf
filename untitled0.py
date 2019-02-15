# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:43:42 2019

@author: suchanekf
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
### We will now define two arrays: r_array will be an array of values for the $CO$ bond length and E_array will hold the electronic energy values corresponding to each separation.
### create an array of 20 bond lengths spanning 0.5 - 3.5 angstroms
### but store in atomic units of length... note 1 angstrom = 1.88973 a.u. of length
r_array = np.linspace(0.561,3.087,20)*1.88973
print(r_array)
### fill in this array with your actual energy values... there should be 20 values in total!!!
E_array = [-107.1389493226,-110.8762342308,-112.2035650482,-112.6221628016,-112.6993448642,-112.6532021548, 
           -112.5695515418,-112.4825450847,-112.4093307577,-112.3611216888, -112.3328706063,-112.3154788092, 
           -112.3040496673,-112.0685479896,-112.2907699794, -112.2869226228,-112.0012243902,-111.9483767861,-111.9274012790,
           -112.2798664306]
# TO see the plot of the PES, uncomment the following lines
plt.plot(r_array, E_array, 'red')
plt.show()

### use cubic spline interpolation
order = 3
### form the interpolator object for the data
sE = InterpolatedUnivariateSpline(r_array, E_array, k=order)
### form a much finer grid
r_fine = np.linspace(1.06,5.0,200)
### compute the interpolated/extrapolated values for E on this grid
E_fine = sE(r_fine)
### plot the interpolated data
plt.plot(r_fine, E_fine, 'blue')
plt.show()

### take the derivative of potential
fE = sE.derivative()
### force is the negative of the derivative
F_fine = -1*fE(r_fine)

### plot the forces
plt.plot(r_fine, np.abs(F_fine), 'red')
plt.xlim(1,5)
plt.show()
