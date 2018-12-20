# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:27:31 2018

@author: Ramana
"""
import RKStat as rst
import numpy as np
import matplotlib.pyplot as plt
x = np.array([63,64,66,66,69,71,71,72,73,75])
y = np.array([127,121,142,157,162,156,169,165,181,208])
rst.who_am_I()
rst.RKLinearRegression(x,y)


