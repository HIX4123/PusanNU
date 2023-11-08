


t = ['anana', 'beer', 'coke', 'duck', 'emu', 'fried', 'beer', 'coke', 'glass']

if 'beer' in t  :
    print('원소가 리스트에 있습니다')
else :
    print('원소가 리스트에 없있습니다')


print(t.index('coke'))

# 조심: 없는 원소에 대해서 index은 오류가 발생합니다.
#print t.index('x')

for i, j in enumerate( t ):
    if j == 'fried':
        print("enumerate index", i)

# index를 리스트로 만들어 봅시다.
indexes = [i for i,x in enumerate(t) if x == 'beer']

print(indexes)



print(t.index('coke'))
print(t.index('coke',2))
print(t.index('coke',4))
#print t.index('coke',4,6) 없는 경우는 오류가 난다. try outofRange error로 처리
print(t.index('coke',-3,-1))


try:
    iit = t.index('coke',4,6)
except ValueError:
    print("Index error 하나 추가 요 !")
    iit = -1



print(iit)

