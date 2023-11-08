
dodo = list(range(11))
soso = list(range(10,30,4))
print("dodo=", dodo)
print("soso=", soso)


print("------ loop 반복하기 ---")
for x in range(10):  # 무조건 10번 반복하기
    print(x, "헤헤")
print('done')

print("------ loop 벗어나기 break ---")
s= 0
for x in range(100):
    s = s + x
    if s > 100: break
    print("s와 x = ", s, x)

print('done')


print("--------- 고급 loop -------")
N = [20, 15, 39, 2, 7, 5, 223, 75, 46, 87]
M = [3, 5, 9, 2, 7]
L = [None] * 10
print("L=", L)

for k in M:
    L[k] = k * N[k]

print("계산후의 L", L)

