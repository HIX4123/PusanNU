#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-03-19
#-------------------------------------------------------------------------------

import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# 예상  CO2 emission 분출양, 무게는 2300kg, 엔진 부피는 1300cm3:
weight = 2300
volume = 1300

outCO2 = regr.predict([[ weight, volume]])

print( f'무게={weight}, 부피={volume}일 때 \n CO2 양={outCO2}')

print("상관계수 = ", regr.coef_)
