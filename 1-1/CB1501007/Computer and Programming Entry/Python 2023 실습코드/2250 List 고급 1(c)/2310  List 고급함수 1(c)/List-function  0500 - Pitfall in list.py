
# List를 사용할 때 주의사항


mystr = ' hello darkness my old friend again '
mybody = [ '김예진', 24, 34, 24, 1.2, 165, 45 ]
mystr = mystr.strip()
print(mystr)
mybody = mybody.sort()  # 이렇게 사용하는 사람이 많다.
#mybody.sort()  # 반드시 이렇게 사용해야 한다. 리스트 자체가 바뀐다.
print(mybody)

t = mystr.split()
x = 'Bomb'
t.append(x)   # 올바른 표현 (O)
print(t)

t = mystr.split()
t = t + [x]   # 올바른 표현 (O)
print(t)

#t.append([x])          # WRONG! (X)
#t = t.append(x)        # WRONG! (X)
#t + [x]                # WRONG! (X)
#t = t + x              # WRONG! (X)
