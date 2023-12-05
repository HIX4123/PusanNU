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
  - $X \sim \text{Geo}(p)$
  - 베르누이 시행에서 처음으로 성공할 때까지의 시행 횟수를 나타내는 분포

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

$\mathbb{E}\left[g\left(X\right)\right]
= \sum\limits_{y\in\Omega_Y}\mathbb{E}\left[g\left(X\right)\mid Y=y\right]\cdot p_Y\left(y\right)$
$\mathbb{E}\left[g\left(X\right)\right] = \int_{-\infty}^{\infty}\mathbb{E}\left[g\left(X\right)\mid Y=y\right]\cdot f_Y\left(y\right)dy$

## 공분산(Covariance)

$\text{Cov}\left(X,Y\right)
= \mathbb{E}\left[\left(X-\mathbb{E}\left[X\right]\right)\left(Y-\mathbb{E}\left[Y\right]\right)\right]
= \mathbb{E}\left[XY\right] - \mathbb{E}\left[X\right]\mathbb{E}\left[Y\right]$

### 공분산 행렬(Covariance Matrix)

분산과 공분산을 나타낸 행렬
$\begin{matrix}
  &X&Y&Z\\
X&\text{Var}\left(X\right)&\text{Cov}\left(X,Y\right)&\text{Cov}\left(X,Z\right)\\
Y&\text{Cov}\left(Y,X\right)&\text{Var}\left(Y\right)&\text{Cov}\left(Y,Z\right)\\
Z&\text{Cov}\left(Z,X\right)&\text{Cov}\left(Z,Y\right)&\text{Var}\left(Z\right)
\end{matrix}$
