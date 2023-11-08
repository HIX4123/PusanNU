
import random
import numpy as np

print(f"> 1. random.random()= {random.random()} ")
print(f"> 2. random.randint(0,10)= {random.randint(0,10)} ")
print(f"> 3. random.uniform(1,5)= {random.uniform(1,5)} ")
print(f"> 4. random.sample(range(0, 32), 5)= {random.sample(range(0, 32), 5)} ")

L1 = [random.random() for _ in range(5)]
print(f"> 5. L1= { L1 } ")


L2 = [random.randint(0,10) for _ in range(5)]
print(f"> 6. L2= { L2 } ")


a= np.random.uniform()
print(f"> 7. { a } ")

a=np.random.uniform(1,5)
print(f"> 8. { a } ")
a=np.random.uniform(1,5,3)
print(f"> 9. { a } ")

a=np.random.randint(1,100, 10)
print(f"> 10. { a } ")

a=np.random.randint(1,6,(5,2))
print(f"> 11. { a } \n a[0]={a[0]}, a[1][1]={a[1][1]}")