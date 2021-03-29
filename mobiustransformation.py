# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:22:45 2021

@author: Alan
"""

import numpy as np
import matplotlib.pyplot as plt

#Mobius Transformation

#number of iterates
numiterates = 10000;

#array storing iterates of mobius transformation
iterates = np.zeros(numiterates,dtype=complex); 

#set starting value
iterates[0] = (-0.5 - 0.5j);

#denote a,b,c,d in f(x) = (ax+b)/(cx+d)
a = 2;
b = 4;
c = 1;
d = -1;

#loop through
for i in range(1, numiterates):
    #if the function goes to infinity
    if(iterates[i-1] == (-d/c)):
        #skip the point at infinity and set iterates[i] to next value (a/c)
        iterates[i] = a/c;
    else:
        #iterate function
        iterates[i] = (a*iterates[i-1] + b) / (c*iterates[i-1]+d);

#make scatterplot on complex plane
plt.scatter(iterates[:].real, iterates[:].imag, s = 10);
plt.show();
        


    



