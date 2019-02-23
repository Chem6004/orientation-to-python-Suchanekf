#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
### create an array of 20 bond lengths spanning 0.5 - 3.5 angstroms
### but store in atomic units of length... note 1 angstrom = 1.88973 a.u. of length
r_array = np.linspace(0.561,3.087,20)*1.88973
print(r_array)

### fill in this array with your actual energy values... there should be 20 values in total!!!
E_array = [-107.1389493226,-110.8762342308,-112.2035650482,-112.6221628016,-112.6993448642,
           -112.6532021548,-112.5695515418,-112.4825450847,-112.4093307577,-112.3611216888,
           -112.3328706063,-112.3154788092,-112.3040496673,-112.0685479896,-112.2907699794,
           -112.2869226228,-112.0012243902,-111.9483767861,-111.9274012790,-112.2798664306]
print(E_array)
# TO see the plot of the PES, uncomment the following lines
plt.plot(r_array, E_array, 'red')
plt.show()
### use order = 5 spline interpolation
order = 5
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
print("First derivative of potential",F_fine,"atomik units")
### plot the forces
plt.plot(r_fine, np.abs(F_fine), 'black')
plt.xlim(1,5)
plt.show()
### Find index of the PES where it has its global minimum
r_eq_idx = np.argmin(E_fine)
### find the value of the separation corresponding to that index
r_eq = r_fine[r_eq_idx]
### print equilibrium bond-length in atomic units and in angstroms
print("Equilibrium bond length is ",r_eq," atomic units")
print("Equilibrium bond length is ",r_eq*0.529," Angstroms")
### get second derivative of potential energy curve... recall that we fit a spline to
### to the first derivative already and called that spline function fE.
cE = fE.derivative()

### evaluate the second derivative at r_eq to get k
k = cE(r_eq)
### define reduced mass of CO as m_C * m_O /(m_C + m_O) where mass is in atomic units (electron mass = 1)
mu = 13625.
w = np.sqrt(k/mu)
### define "ground-state" velocity:
v = np.sqrt( np.sqrt(k/mu)/(2*mu))
### get random position and velocity for CO within a reasonable range
r_init = np.random.uniform(0.75*r_eq,2*r_eq)
v_init = np.random.uniform(-2*v,2*v)

### print initial position and velocity
print("Reduced mass is",mu,"atomic units")
print("Vibrational frequency is",w,"atomic units")
print("Initial separation is ",r_init, "atomic units")
print("Initial velocity is   ",v_init, "atomic units")
print("force factor is  ",k, "atomic units")
### establish time-step for integration to be 0.2 atomic units... this is about 0.01 femtoseconds
dt = 0.02

### get force on particle 
F_init = -1*fE(r_init)
def Velocity_Verlet(r_curr, v_curr, mu, f_interp, dt):
    ### get acceleration at current time
    a_curr = -1*f_interp(r_curr)/mu
    
    ### use current acceleration and velocity to update position
    r_fut = r_curr + v_curr * dt + 0.5 * a_curr * dt**2
    
    ### use r_fut to get future acceleration a_fut
    a_fut = -1*f_interp(r_fut)/mu
    ### use current and future acceleration to get future velocity v_fut
    v_fut = v_curr + 0.5 * a_curr * dt + 0.5 * a_fut * dt
    
    result = [r_fut, v_fut]
    
    return result

### how many updates do you want to perform?
N_updates = 200000

### Now use r_init and v_init and run velocity verlet update N_updates times, plot results
### these arrays will store the time, the position vs time, and the velocity vs time
r_vs_t = np.zeros(N_updates)
v_vs_t = np.zeros(N_updates)
t_array = np.zeros(N_updates)

### first entry is the intial position and velocity
r_vs_t[0] = r_init
v_vs_t[0] = v_init

### first Velocity Verlet update
result_array = Velocity_Verlet(r_init, v_init, mu, fE, dt)

### do the update N_update-1 more times
for i in range(1,N_updates):
    tmp = Velocity_Verlet(result_array[0], result_array[1], mu, fE, dt)
    result_array = tmp
    t_array[i] = dt*i
    r_vs_t[i] = result_array[0]
    v_vs_t[i] = result_array[1]

### Plot the trajectory of bondlength vs time:
plt.plot(t_array, r_vs_t, 'red')
plt.show()

### plot the phase space trajectory of position vs momentum
plt.plot(mu*v_vs_t, r_vs_t, 'blue')
plt.show()
a = -1*fE(3)/mu
print("Accelaration is ",a,"atomik units")
