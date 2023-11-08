


a = 3 + 4j
b = 10 - 5j
c = 5 +1j  # 그냥 j만 쓰면 오류가 남. 반드시 1j

print("\n 다양한 복소수 계산")
cla= [a, b, a*b, a/b, abs(a), abs(b), a*b*c, a/b/c ]

for w in cla :
    print(f"{w.real:10.5f} + {w.imag:10.5f}i")


