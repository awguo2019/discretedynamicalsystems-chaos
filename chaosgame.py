# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:20:09 2021

@author: Alan
"""

import numpy as np
import matplotlib.pyplot as plt
from random import seed
from random import randint
import operator

# seed random number generator
seed(1)

iterates = np.zeros((10000, 2)); #array storing iterates of chaos game

transform = np.array([[1/3, 0],[0, 1/3]]); #transformation matrix

points = np.array([[0, 1], [1, 0], [0,0], [1,1], [0.5, 1], [1, 0.5], [0.5, 0], [0,0.5]]); #array storing attracting points
num_points = np.shape(points)[0]; #number of attracting points

iterates[0] = (0.5, 0.5); #set the starting point

for i in range(1, 10000): #iterate 5000 times, starting at (0,0)
    
    rand = randint(0, num_points-1); #choose random point to move towards
   
    (x, y) = tuple(map(operator.sub, iterates[i-1], points[rand])); #get difference of prev iterate and attracting point

    (x, y) = np.matmul(transform, (x,y)); #multiply difference w transform matrix

    (x, y) = tuple(map(operator.add, (x,y), points[rand])); #add the attracting point 
    
    iterates[i] = (x,y); #set iterates[i] equal to our x,y


plt.scatter(iterates[:,0], iterates[:,1]); #make scatterplot w columns being axes
plt.show();

    