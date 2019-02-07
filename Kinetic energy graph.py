#!/usr/bin/env python3
# -*- coding: utf-8 -*-
  
import time
### import pyplot as library
from matplotlib import pyplot as plt
### get the time at the beginning of the program
start = time.time()
### create an array of 100 x-values between -5 and 5
x = np.linspace(-5,6,100)
### create an array of y-values defined as y = x^2
y = 0.5*x**2
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

