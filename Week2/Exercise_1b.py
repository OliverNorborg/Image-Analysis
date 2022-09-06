#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:53:52 2022

@author: olivernorborg
"""

"""
Help with exercises:
Exercise 4 - Clarification fo covarience and the plot
Exercise 6 - Have i found the right covariance in exercise 5?

"""

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import decomposition

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

#Saves the image -uncomment to save
#plt.savefig('pairplot.png')
plt.show()

# What measurements are related and which ones are not-related? 
#   Sepal elngth a width seem to have a linear correlation
#Can you recognise the results you found, when you computed the variance and covariance?
#   Not really...?

"""Exercise 5 - PCA"""
#Subtracting the mean from the data
mn = np.mean(x, axis=0)
data = x - mn

sep_l_data = data[:, 0]
sep_w_data = data[:, 1]
pet_l_data = data[:, 2]
pet_w_data = data[:, 3]

C_sep = (1/(n_obs-1))*np.matmul(sep_l_data, np.transpose(sep_w_data))
C_sep_l = (1/(n_obs-1))*np.matmul(sep_l_data, np.transpose(sep_l_data))
C_sep_w = (1/(n_obs-1))*np.matmul(sep_w_data, np.transpose(sep_w_data))
C_pet = (1/(n_obs-1))*np.matmul(pet_l_data, np.transpose(pet_w_data))
C_pet_l = (1/(n_obs-1))*np.matmul(pet_l_data, np.transpose(pet_l_data))
C_pet_w = (1/(n_obs-1))*np.matmul(pet_w_data, np.transpose(pet_w_data))
print("C_Sep:",C_sep)
print("C_sep_l:", C_sep_l)
print("C_sep_w:", C_sep_w)
C_sep_matrix = np.array([[C_sep_l,C_sep],[C_sep, C_sep_w]])
print("Own result:")
print(C_sep_matrix)
print("np.cov result:")
print(np.cov(sep_l_data,sep_w_data))

c_x = np.cov(data.T)


"""Exercise 6 - Principle componets"""
#eig(covaraince matrix), which covaraince matrix?
values, vectors = np.linalg.eig(c_x)

"""Exercise 7 - """
#Values are found in the above exercise

v_norm = values.cumsum() / values.sum() * 100
v_norm = np.insert(v_norm,0,0)
plt.plot(v_norm)
plt.xlabel('Principal component')
plt.ylabel('Percent explained variance')
plt.ylim([0, 100])
plt.show()

"""Exercise 8 - Projecting data onto PCA space"""
pc_proj = vectors.T.dot(data.T)
# plt.figure()
# d2 = pd.DataFrame(pc_proj)
# sns.pairplot(d2)
# plt.show()

"""Exercise 9 - A different way to find PCA"""
pca = decomposition.PCA()
pca.fit(x)
values_pca = pca.explained_variance_
exp_var_ratio = pca.explained_variance_ratio_
vectors_pca = pca.components_
data_transform = pca.transform(data)





















