

L = [w for w in range(1,300) if w%13 == 0 ]
print(L)


G = (w for w in range(1,300) if w%13 == 0 )
print("Generator G()= ", G)


print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))

#왜 generator를 사용하는가 ? 필요할 때만 꺼내 사용한다.
#미리 다 만들어 두는 것이 아니라...

G = (w for w in range(1,500) if w%17 == 0 )
i=0

try:
    while (True):
        i += 1
        print(f"i={i:3}  {next(G)}")
except StopIteration:
    pass



