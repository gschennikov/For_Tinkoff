#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
import numpy as np
import random
from IPython.display import clear_output
from time import sleep


# In[3]:


def mates(i,j):
    mates = []
    mates.append([i-1,j-1])
    mates.append([i-1,j+1])
    mates.append([i+1,j-1])
    mates.append([i+1,j+1])
    mates.append([i-1,j])
    mates.append([i+1,j])
    mates.append([i,j-1])
    mates.append([i,j+1])
    return mates

matrix = [[0 for x in range(31)] for y in range(31)]

for i in range(1,30):
    for j in range(1,30):
        matrix[i][j] = random.choice(['S', 'F', 'R', 'N'])
            
matrix_old = matrix.copy()
matrix_new = matrix.copy()

alive = True

while alive:
    for row in matrix_old:
        print(*row)
    shrimpes_list = []
    fishes_list = []
    for i in range(1,30):
        for j in range(1,30):
            if matrix_old[i][j] == 'S':
                shrimpes_list.append([i,j])
            if matrix_old[i][j] == 'F':
                fishes_list.append([i,j])
    alive =False
    if (len(fishes_list)>0) or (len(shrimpes_list)>0):
        alive = True
    for i in range(1,30):
        for j in range(1,30):
            if matrix_old[i][j] == 'F':
                matrix_new[i][j] = 'F'
                fishcounter = 0
                for k in range(8):
                    if mates(i,j)[k] in fishes_list:
                        fishcounter+=1
                if fishcounter>3 or fishcounter<3:
                    matrix_new[i][j] = 'N'
            if matrix_old[i][j]=='R':
                matrix_new[i][j] = 'R'
            if matrix_old[i][j] == 'N':
                matrix_new[i][j] = 'N'
                fishcounter = 0
                shrimpcounter = 0
                for k in range(8):
                    if mates(i,j)[k] in fishes_list:
                        fishcounter +=1
                if fishcounter == 3:
                    matrix_new[i][j]='F'
                for k in range(8):
                    if mates(i,j)[k] in shrimpes_list:
                        shrimpcounter +=1
                if shrimpcounter == 3:
                    matrix_new[i][j]='S'
            if matrix_old[i][j] == 'S':
                matrix_new[i][j] = 'S'
                shrimpcounter = 0
                for k in range(8):
                    if mates(i,j)[k] in shrimpes_list:
                        shrimpcounter+=1
                if shrimpcounter>3 or shrimpcounter<3:
                    matrix_new[i][j] = 'N'
    sleep(3)
    clear_output()
    matrix_old = matrix_new.copy()


# In[ ]:




