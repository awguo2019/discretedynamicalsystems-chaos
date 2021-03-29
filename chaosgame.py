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

#number of iterates
numiterates = 100000;

#array storing iterates of chaos game
iterates = np.zeros((numiterates, 2)); 

#transformation matrix
transform = np.array([[1/3, 0],
                      [0, 1/3]]); 

#array storing attracting points
points = np.array([[1, 0.5],  
                   [0.5,0],
                   [0, 0.5],
                   [0.5, 1]]); 

#number of attracting points
num_points = np.shape(points)[0]; 

#set the starting point
iterates[0] = (.5, 0.5); 

#iterate 5000 times, starting at (0,0)
for i in range(1, numiterates): 
    #choose random point to move towards
    rand = randint(0, num_points-1); 
   #get difference of prev iterate and attracting point
    (x, y) = tuple(map(operator.sub, iterates[i-1], points[rand])); 
    #multiply difference w transform matrix
    (x, y) = np.matmul(transform, (x,y)); 
    #add the attracting point
    (x, y) = tuple(map(operator.add, (x,y), points[rand]));  
    #set iterates[i] equal to our x,y
    iterates[i] = (x,y); 

#make scatterplot w columns being axes (skips the first 12 points)
plt.scatter(iterates[12:,0], iterates[12:,1], s = 1);
plt.show();

    
