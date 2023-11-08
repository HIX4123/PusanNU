#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-03-19
#-------------------------------------------------------------------------------

import pandas
from sklearn import linear_model

df = pandas.read_csv("mydata.csv")

X = df[['Pic', 'Char']]
y = df['Reply']

regr = linear_model.LinearRegression()
regr.fit(X, y)


mypic = 3   # 그림이 3개이고
mychar = 33  # 글자수가 33글자이면

expreply = regr.predict([[ mypic, mychar]])

print( f'그림수 ={mypic}, 글자수={mychar}일 때 \n 예상 댓글수={expreply}')

print("상관계수 = ", regr.coef_ )
print( f'그림당 추가  댓글 수  = {regr.coef_[0]:.5f}' )
print( f'글자당 추가  댓글 수  = {regr.coef_[1]:.5f}'  )
