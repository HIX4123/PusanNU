#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-03-19
#-------------------------------------------------------------------------------

import pandas as pd

df = pd.read_csv("manhattan.csv")
df.head()


# 데이터 세트 분리는 sklearn에서 train_test_split을 통해 손쉽게 할 수 있다.
# 아래와 같이 8:2 정도의 비율로 나눠보자.

from sklearn.model_selection import train_test_split
x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
y = df[['rent']]
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

from sklearn.linear_model import LinearRegression
mlr = LinearRegression()
mlr.fit(x_train, y_train)

# 이제 만약 내가 주택에 대한 14개 항목값 넣어주면 주택 임대료를 예측해준다.
my_apartment = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 1, 1, 0]]
my_predict = mlr.predict(my_apartment)

#> expected [[2393.58059075]]

# 이제 x 시험 데이터 x_test를 넣어 예측한 y 값들을 y_predict라고 저장해보자.
# 추후에 시험 데이터에 있는 실제 정답, 즉 y_test와 비교해보기 위함이다.
y_predict = mlr.predict(x_test)

# matplotlib의 시각화를 통해 간단히 확인하고 넘어가보자.

# x축은 실제 임대료, y축은 예측한 임대료다.
# 만약 정답을 맞춘다면 정확히 선으로 일치되어 나올 거다.

# 그런데 다중회귀에서는 변수가 많기 때문에 조금 표현을 달리해야겠다.
# 일단 모든 변수 x마다 각각의 m이 있다. 그러니 이것들을 회귀계수라고 부르자.
# 그리고 b는 그냥 상수라고 부르자.

# 아무튼 다중회귀에서도 단순회귀와 똑같이 이 값들을 확인할 수 있다.
# 모델 뒤에 .coef_ , .intercept_라고 써주면 끝이다.
print("상관계수 =", mlr.coef_ )

for i,w in enumerate(mlr.coef_[0]) :
    print(f'i={i:3d}, coef= {w:10.6f}')

import matplotlib.pyplot as plt
plt.scatter(y_test, y_predict, alpha=0.2)
plt.xlabel("Actual Rent")
plt.ylabel("Predicted Rent")
plt.title ("MULTIPLE LINEAR REGRESSION")
plt.show( )


# 주택의 면적 'size_sqft'과 가격 'rent'
plt.xlabel("Rental Price")
plt.ylabel("Size Square Fit")
plt.title ("MULTIPLE LINEAR REGRESSION")
plt.scatter(df[['size_sqft']], df[['rent']], color="green", alpha=0.2)
plt.show()

"""
모델의 정확도(Accuracy) 평가하기
위에서 데이터 세트를 나눠놨기 때문에 학습 시킨 모델을 테스트 할 수 있다.
다중선형회귀 모델의 정확도를 평가할 때는 잔차 분석(Analysis)을 하면 된다. 잔차는 실제 값 y와 예측된 값 ŷ의 차 e를 말한다. 방정식으로 표현하면 이렇게.
sklearn의 linear_model.LinearRegression를 사용해서 모델을 생성하면 .score()라는 메서드를 사용할 수 있는데 R²라고 하는 결정계수(coefficient of determination)를 돌려준다. 결정계수 R²은 이렇게 표현할 수 있다.


일단 분자에 있는 u는 잔차의 제곱의 평균 RSS(residual sum of square)는 직선이 미처 Y에 대해 설명하지 못한 변화량을 의미한다.
((y - y_predict) ** 2).sum()

분모에 있는 v는 TSS(total sum of squares), y값의 총 변화량으로 이해하면 된다.
((y - y.mean()) ** 2).sum()

결국 결정계수 R²는 전체에서 직선이 미처 설명하지 못한 부분의 비율을 뺀 거다.
아무튼 어려우면 다 잊고 그냥…….
결정계수 R²가 클수록 실제값과 예측값이 유사함을 의미하며, 데이터를 잘 설명한다고 이해하자.
그러니 모델이 얼마나 정확한지 평가할 때도 이 결정계수 R²가 기준이 될 수 있는 거다.
예를 들어, 주택 사이즈(“size_sqft”)와 침실 개수(“bedrooms”)를 기준으로
임대료를 예측하는 모델의 R²이 0.72인 경우 그 2개의 변수들이 함께
임대료 변동의 72%를 설명한다는 뜻이다.
여기에 다른 x 변수, 주택이 얼마나 오래 전에 지어졌는지(“building_age_yrs”)를
모델에 추가하면 새로운 R²가 0.95로 증가했다고 하자.
그럼 주택 사이즈(“size_sqft”), 침실 개수(“bedrooms”),
얼마나 오래 전에 지어졌는지(“building_age_yrs”) 이 3개의 변수가 함께 임대료
변동의 95%를 설명한다는 거다.
당연히 최선의 R²는 1이겠지만 그건 말이 안 되고, 일반적으로 0.7 정도면 양호한 것으로 간주한다.
위 예제에서 14개의 변수를 넣고 생성한 모델의 결정계수를 확인해보자.
"""

#print( f' RSS= {((y - y_predict) ** 2).sum()}')
#print( f' TSS= {((y - y.mean()) ** 2).sum() }')

print("mlr score=", mlr.score(x_train, y_train))

# 꽤 높다.
# 즉 주택 임대료의 77%를 저 14개의 항목으로 설명할 수 있다는 의미다.