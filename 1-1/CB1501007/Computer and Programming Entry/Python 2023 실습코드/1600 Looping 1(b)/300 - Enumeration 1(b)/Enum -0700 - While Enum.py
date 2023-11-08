

sum = 0  # 합계를 구하는 전형적인 방법
a = 0
while a < 10: # while의 조건부 문장이 참(true)일 동안 계속 돌아간다
    a = a + 1
    print(a, end=' ')
    sum = sum + a

# while loop을 벋어남.
print("\n 전체 합계는 = ", sum, '\n')

# while02.py
a = 0
while a < 10:
    a = a + 1
    if a < 3: continue
    if a > 10: break
else:
    print('else block')

# while loop을 벋어남.
print('done while experiment')

