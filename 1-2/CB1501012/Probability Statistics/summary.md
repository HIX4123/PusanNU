# Summary

하 기 싫 다

## 배경지식

### 이산 분포(Discrete Distributions)

- 균일 분포(Uniform)
  - $X \sim \text{Unif}(a, b)$
  - $a$와 $b$ 사이의 모든 값이 나올 확률이 동일한 분포
- 베르누이 분포(Bernoulli)
  - $X \sim \text{Ber}(p)$
  - $p$의 확률로 1을 가지고, $1-p$의 확률로 0을 가지는 분포
- 이항 분포(Binomial)
  - $X \sim \text{Bin}(n, p)$
  - $n$번의 베르누이 시행을 했을 때, $p$의 확률로 1을 가지는 횟수를 나타내는 분포
- 푸아송 분포(Poisson)
  - $X \sim \text{Poi}(\lambda)$
  - 단위 시간당 평균 $\lambda$번 발생하는 사건이 단위 시간당 $k$번 발생할 확률을 나타내는 분포
- 기하적 분포(Geometric)
  - $X \sim \text{Geo}(p) = \left(1-p\right)^{k-1}p$
  - 베르누이 시행에서 처음으로 성공할 때까지의 시행 횟수를 나타내는 분포
  - $E\left[X\right] = \dfrac{1}{p},\,\text{Var}\left(X\right) = \dfrac{1-p}{p^2}$

### 연속 분포(Continuous Distributions)

- 균일 분포(Uniform)
  - $X \sim \text{Unif}(a, b)$
  - $a$와 $b$ 사이의 모든 값이 나올 확률이 동일한 분포
- 지수 분포(Exponential)
  - $X \sim \text{Exp}(\lambda)$
  - 단위 시간당 평균 $\lambda$번 발생하는 사건(푸아송 과정)이 단위 시간당 $t$ 시간 이내에 발생할 확률을 나타내는 분포
- 정규 분포(Normal)
  - $X \sim \text{N}(\mu, \sigma^2)$
  - 평균이 $\mu$이고 분산이 $\sigma^2$인 분포

## 집합의 데카르트곱(Cartesian Product of Sets)

- $A \times B = \{(a, b) \mid a \in A, b \in B\}$
- ex) $A = \{1, 2\}, B = \{a, b\} \Rightarrow A \times B = \{(1, a), (1, b), (2, a), (2, b)\}$

## 결합확률질량함수(Joint PMFs)

- 두 개 이상의 확률변수를 동시에 고려하는 확률질량함수
- $p_{X, Y}(x, y) = P(X = x, Y = y)$
- 결합범위 $\Omega_{X\times Y}\{\left(c, d\right): p_{X, Y}\left(c, d\right) > 0\} \subseteq \Omega_X\times\Omega_Y$
- $E\left[g\left(X,Y\right)\right] = \sum\limits_x\sum\limits_y g\left(x,y\right)\cdot p_{X,Y}\left(x,y\right)$

## 주변확률질량함수(Marginal PMFs)

- 결합확률질량함수에서 하나의 확률변수에 대한 확률질량함수
- $p_X\left(a\right) = \sum\limits_{b\in\Omega_Y}p_{X,Y}\left(a,b\right)$
  - $x = a$일 때, $y$의 모든 값에 대한 확률을 더함

## 독립(Independence)

- 두 확률변수 $X$와 $Y$가 독립이라는 것은 $X$의 값이 $x$일 때 $Y$의 값이 $y$일 확률이 $X$의 값이 $x$일 때 $Y$의 값이 $y$일 조건부 확률과 같다는 것을 의미
- $p_{X,Y}\left(x,y\right) = p_X\left(x\right)p_Y\left(y\right)$

## 이산조건부분포(Discrete Conditional Distribution)

- $P\left(E\mid F\right) = \frac{P\left(E\cap F\right)}{P\left(F\right)} = \frac{P\left(EF\right)}{P\left(F\right)}$

## 연속조건부분포(Continuous Conditional Distribution)

- $f_{Y\mid X=x}\left(y\right) = \frac{f_{XY}\left(x,y\right)}{f_X\left(x\right)}$

## 조건부 기댓값(Conditional Expectation)

- $E\left[X\mid Y=y\right] = \sum\limits_{x\in\Omega_X}x\mathbb{P}\left(X=x\mid Y=y\right) = \sum\limits_{x\in\Omega_x}xp_{X,Y}\left(x\mid y\right)$

## 총 기댓값의 법칙(Law of Total Expectation)

$E\left[g\left(X\right)\right]
= \sum\limits_{y\in\Omega_Y}E\left[g\left(X\right)\mid Y=y\right]\cdot p_Y\left(y\right)$
$E\left[g\left(X\right)\right] = \int_{-\infty}^{\infty}E\left[g\left(X\right)\mid Y=y\right]\cdot f_Y\left(y\right)dy$

## 공분산(Covariance)

$\text{Cov}\left(X,Y\right)
= E\left[\left(X-E\left[X\right]\right)\left(Y-E\left[Y\right]\right)\right]
= E\left[XY\right] - E\left[X\right]E\left[Y\right]$

- $X\perp Y \Rightarrow \text{Cov}\left(X,Y\right) = 0$
- $\text{Cov}\left(X,X\right) = \text{Var}\left(X\right)$
- 대칭성: $\text{Cov}\left(X,Y\right) = \text{Cov}\left(Y,X\right)$
- 비선형성: $\text{Cov}\left(aX+bY,Z\right) = a\text{Cov}\left(X,Z\right) + b\text{Cov}\left(Y,Z\right)\, \approx$ 분배법칙
- 분산합: $\text{Var}\left(X+Y\right) = \text{Var}\left(X\right) + 2\text{Cov}\left(X,Y\right) + \text{Var}\left(Y\right)\,\approx$ 제곱의 합

### 공분산 행렬(Covariance Matrix)

분산과 공분산을 나타낸 행렬
$\begin{matrix}
  &X&Y&Z\\
X&\text{Var}\left(X\right)&\text{Cov}\left(X,Y\right)&\text{Cov}\left(X,Z\right)\\
Y&\text{Cov}\left(Y,X\right)&\text{Var}\left(Y\right)&\text{Cov}\left(Y,Z\right)\\
Z&\text{Cov}\left(Z,X\right)&\text{Cov}\left(Z,Y\right)&\text{Var}\left(Z\right)
\end{matrix}$

## 상관계수(Correlation Coefficient)

$\rho\left(X, Y\right) = \dfrac{\text{Cov}\left(X,Y\right)}{\sigma_X\sigma_Y} \in \left[-1, 1\right]$

## 모집단과 표본(Population and Sample)

- 모집단 $N$: 관심 대상이 되는 모든 개체의 집합
- 표본 $n$: 모집단의 부분집합

## 표본평균과 표본분산(Sample Mean and Variance)

$\begin{matrix}
  &\text{Population}&\text{Sample}\\
\text{Mean}&\mu = E\left[X\right]&\bar{x} = \dfrac{1}{n}\sum\limits_{i=1}^nx_i\\
\text{Variance}&\sigma^2 = \text{Var}\left(X\right)&s^2 = \dfrac{1}{n-1}\sum\limits_{i=1}^n\left(x_i-\bar{x}\right)^2
\end{matrix}$

## 큰 수의 법칙(Law of Large Numbers)

- 표본의 크기가 커질수록 표본평균이 모평균에 가까워짐

## 독립동일분포확률변수(Independent and Identically Distributed Random Variables)

$X_1\perp X_2\perp \cdots\perp X_n,\,X_1 \sim X_2 \sim \cdots \sim X_n\\\Rightarrow X_1, X_2, \cdots, X_n \sim \text{iid}$

## 중심극한정리(Central Limit Theorem)

$X_1, X_2, \cdots, X_n \sim \text{iid},\,E\left[X_i\right] = \mu,\,\text{Var}\left(X_i\right) = \sigma^2\\$

$\Rightarrow \bar{X} = \dfrac{1}{n}\sum\limits_{i=1}^nX_i \sim \text{N}\left(\mu, \dfrac{\sigma^2}{n}\right)$

- $\sum\limits_{i=1}^n X_i\sim N\left(n\mu, n\sigma^2\right)$
- Binomial RV
  - $X \sim \text{Bin}\left(n, p\right) \Rightarrow X \sim \text{N}\left(np, np\left(1-p\right)\right)$
- Uniform RV
  - $X \sim \text{Unif}\left(a, b\right) \Rightarrow X \sim \text{N}\left(\dfrac{a+b}{2}, \dfrac{\left(b-a\right)^2}{12}\right)$

