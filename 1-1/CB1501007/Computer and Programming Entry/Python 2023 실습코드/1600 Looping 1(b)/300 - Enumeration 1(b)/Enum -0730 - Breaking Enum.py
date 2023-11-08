
for x in range(10):
    if x < 8: continue  # x < 8 이면 for 문으로 다시 올라간다.
    print(x)
print('done 2')

for x in range(10):
    print(x, end=' ')   # , 이 있을때와 없을 때를 비교해보자
else:
    print('else block')
print('done 3')

for x in range(10):
    break
    print(x, end=' ')   # for loop에도 ELSE 가 적용될 수 있는 예제
else:
    print('else block')
print('done 4')

# for09.py
lt = [('one', 1), ('two', 2), ('three', 3)]
for t in lt:
    print('name=', t[0], 'num=', t[1])

print("--------- an important experi. --------")
x = [1, 3, -7, 4, 9, -5, 4]
for i, n in enumerate(x):
    if n < 0:
        print("A negative number = %d at index %d" % (n, i))