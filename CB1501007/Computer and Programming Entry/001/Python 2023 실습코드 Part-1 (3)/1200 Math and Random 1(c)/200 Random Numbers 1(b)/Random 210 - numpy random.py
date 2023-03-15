
import numpy as np

S1 = np.random.randint(11)  # [0에서 10까지의 random numbe 1ro
S2 = np.random.rand(10, 2)  #  10개, 2차원 normal uniform

print(f"\n S1= {S1}")
print(f"\n S2= {S2}")

m,n= 6, 2
S3 = np.random.randn( m,n) # 평균 0, 펴준편차 1인 Gauusian 차원은 m by n matrix
print(f"\n S3= {S3}")

start= 100
stop = 500
rows = 8
columns = 3

S4 = np.random.uniform(start,stop,(rows,columns))
print(f"\n S4= {S4}")