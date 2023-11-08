
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', family='NanumGothic')  # 한글 폰트 설정

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel(u' 개인별 IQ 수치', color='red')
plt.ylabel('확률값', color='red')
plt.title(' 히스토그램(Histogram) of IQ', color='blue')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()