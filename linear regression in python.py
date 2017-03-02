#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:25:57 2017

@author: zoe
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
data = pd.read_csv('~/Documents/brunhild.txt', sep="\t", header = None)
hour = data[0]
hour[0] = 0
hour = hour.apply(pd.to_numeric)
sulfate = data[1]
sulfate[0] = 0
sulfate = sulfate.apply(pd.to_numeric)
hour = np.array(hour)
hour = np.delete(hour,0)
sulfate = np.array(sulfate)
sulfate = np.delete(sulfate,0)
hours = pd.DataFrame(hour)
regr = linear_model.LinearRegression()
regr.fit(hours, sulfate)
# The coefficients
print('Coefficients: \n', regr.coef_)
print("Mean squared error: %.2f"
      % np.mean((regr.predict(hours) - sulfates) ** 2))
print('Variance score: %.2f' % regr.score(hours, sulfates))
