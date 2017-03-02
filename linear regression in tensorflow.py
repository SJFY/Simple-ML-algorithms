#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 21:19:19 2017

@author: zoe
"""
import tensorflow as tf
import numpy as np
from numpy import genfromtxt
import pandas as pd
import matplotlib.pyplot as plt
import math 
from math import log
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
hours = [log(y) for y in hour]
sulfates = [log(y) for y in sulfate]
# Model parameters
W = tf.Variable([-.3], tf.float32)
b = tf.Variable([.3], tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)
# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.001)
train = optimizer.minimize(loss)
# training data
x_train = hours
y_train = sulfates
# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong
for i in range(1000):
  sess.run(train, {x:x_train, y:y_train})

# evaluate training accuracy
curr_W, curr_b, curr_loss  = sess.run([W, b, loss], {x:x_train, y:y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))
y_pred = curr_W*x_train +curr_b 
plt.plot(x_train,y_pred)
#plt.plot(x_train,y_train)
#plt.axis([0,175,0,16])

plt.show()