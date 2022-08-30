#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:53:52 2022

@author: olivernorborg
"""

import numpy as np
in_dir = "data/"
txt_name = "irisdata.txt"
iris_data = np.loadtxt(in_dir + txt_name, comments="%")
# x is a matrix with 50 rows and 4 columns
x = iris_data[0:50, 0:4]

"""Exercise 1 - Intro to PCA"""
n_feat = x.shape[1]
n_obs = x.shape[0]
print(f"Number of features: {n_feat} and number of observations: {n_obs}")

"""Exercise 2 - Variance"""

sep_l = x[:, 0]
sep_w = x[:, 1]
pet_l = x[:, 2]
pet_w = x[:, 3]

# Use ddof = 1 to make an unbiased estimate
var_sep_l = sep_l.var(ddof=1)
var_sep_w = sep_w.var(ddof=1)
var_pet_l = pet_l.var(ddof=1)
var_pet_w = pet_w.var(ddof=1)
print("Variance of sepal length: ", var_sep_l)
print("Variance of sepal width: ", var_sep_w)
print("Variance of petal length: ", var_pet_l)
print("Variance of petal width: ", var_pet_w)  

"""Exercise 3 - Covariance"""


