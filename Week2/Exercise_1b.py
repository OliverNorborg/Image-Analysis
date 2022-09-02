#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:53:52 2022

@author: olivernorborg
"""

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

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

length_product = 0
width_product = 0 
for i in range(n_obs):
    length_product = length_product + (sep_l[i] * pet_l[i])
    width_product = width_product + (sep_w[i] * pet_w[i])

Cov_length = (1/(n_obs - 1)) * length_product
Cov_width = (1/(n_obs - 1)) * width_product
print("Covariance for the length between sepal and petal is: ", Cov_length)
print("Covariance for the width between sepal and petal is: ", Cov_width)

"""Exercise 4 - """

plt.figure() # Added this to make sure that the figure appear
# Transform the data into a Pandas dataframe
d = pd.DataFrame(x, columns=['Sepal length', 'Sepal width','Petal length', 'Petal width'])
sns.pairplot(d)
plt.show()

