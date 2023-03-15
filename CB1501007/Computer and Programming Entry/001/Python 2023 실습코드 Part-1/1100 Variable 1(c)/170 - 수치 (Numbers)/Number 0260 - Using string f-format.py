

import math

v=math.factorial(20)

print(f">1. v={v}")  # 2432902008176640000
print(f">2. v= {v:.5f}")
print(f">3. v={v:.4e}") # 2.4329020e+18
print(f">4. v={v:7.5e}") # 2.4329020e+18
print(f">5. v={v:8.3e}") # 2.4329020e+18



for w in range(10,21):
    print(f"w={w},  {math.factorial(w):.3e}")



