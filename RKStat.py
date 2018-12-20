# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:26:32 2018

@author: Ramana
"""
import numpy as np
import matplotlib.pyplot as plt

def who_am_I():
 print("Ramana Statistics")
 
def RKLinearRegressionone():
    ht = np.array([63,64,66,66,69,71,71,72,73,75])
    print (ht)
    wt = np.array([127,121,142,157,162,156,169,165,181,208])
    print (wt)
    sl = -266.53 + 6.1376 * ht

    sl2 = -331.2 + 7.1 * ht
    print("print sl")
    print (sl)
    print("print sl2")
    print(sl2)
    prederr = ( sl - sl2)
    sqrd_prederr = ( sl - sl2) ** 2
    print(prederr)
    print(sqrd_prederr)
    plt.scatter(ht,wt)
    plt.plot(ht,sl)
    plt.plot(ht,sl2)
    print ("Sum of squared predicted errors 1 :" ,np.sum(sl))
    print ( "Sum of squared predicted errors 2 :", np.sum(sl2))
    if np.sum(sl) < np.sum(sl2) :
      print ( " s1 prediction is good")
    else:
     print ( " s1 prediction is good")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    
def RKLinearRegression(x,y):
    print(x)
    print(y)
    sl = -266.53 + 6.1376 * x

    sl2 = -331.2 + 7.1 * x
    print("print sl")
    print (sl)
    print("print sl2")
    print(sl2)
    prederr = ( sl - sl2)
    sqrd_prederr = ( sl - sl2) ** 2
    print(prederr)
    print(sqrd_prederr)
    plt.scatter(x,y)
    plt.plot(x,sl, label="prediction 1")
    plt.plot(x,sl2, label="prediction 2")
    plt.legend(loc='upper left')
    print ("Sum of squared predicted errors 1 :" ,np.sum(sl))
    print ( "Sum of squared predicted errors 2 :", np.sum(sl2))
    if np.sum(sl) < np.sum(sl2) :
      print ( " prediction  1 is good")
    else:
     print ( " prediction 2 is good")
    plt.xlabel("Height")
    plt.ylabel("Weight")
