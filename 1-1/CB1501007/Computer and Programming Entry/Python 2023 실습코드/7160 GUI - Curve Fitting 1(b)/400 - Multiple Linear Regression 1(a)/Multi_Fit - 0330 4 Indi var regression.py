#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-03-19
#-------------------------------------------------------------------------------
# https://aegis4048.github.io/mutiple_linear_regression_and_visualization_in_python


import pandas as pd
import numpy as np
from sklearn import linear_model

file = 'https://aegis4048.github.io/downloads/notebooks/sample_data/unconv_MV_v5.csv'
df = pd.read_csv(file)

features = ['Por', 'Brittle', 'Perm', 'TOC']
target = 'Prod'

X = df[features].values.reshape(-1, len(features))
y = df[target].values

ols = linear_model.LinearRegression()
model = ols.fit(X, y)

print( "4개 변수의 계수 = ", model.coef_ )
print( "절편 = ", model.intercept_ )

"""
Accuracy assessment: R2
In the same we evaluated model performance
with 2D linear model above,
we can evaluate the 3D+ model performance
with R-squared with model.score(X, y).
X is the features, and y is the response
variable used to fit the model.

model.score(X, y)

"""

print( "오차= ",model.score(X, y) )