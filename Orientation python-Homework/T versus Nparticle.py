#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#importing the required module 
import matplotlib.pyplot as plt 
# x axis values 
x = [15,30,45,60,75] 
# corresponding y axis values 
y = [91.9,183.8,275.6,367.5,459.3]   
# plotting the points  
plt.plot(x, y) 
# naming the x axis 
plt.xlabel('N-Particle') 
# naming the y axis 
plt.ylabel('Total Kinetik Energy') 
  
# giving a title to my graph 
plt.title('T_vs_Npart') 
  
# function to show the plot 
plt.show() 


