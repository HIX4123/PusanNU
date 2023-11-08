

m=[[5, 4, [[]] ], [ -999, [88.99 ,9] ], [],  [ ["a"] , "bb", "ccc"]]


print("Last of last ==> ",m[-1][-1])

m[-1][0].append("IPA")
print("Out 1 ==> ",m)

print("Out 2 ==> ",  m[0], m[1])
print("Out 3 ==> ",  m[0], m[1])
print("Out 4 ==> ", m[1][1], m[3][0])


m.append( [-10, -20, -30 ])

print("Out 5 ==> ",m)


m[0].append( [-10, -20, -30 ])
print("Out 6 ==> ",m)

m[0][2].append( ["PIG" ])
print("Out 7 ==> ",m)

print("어떤 원소를 모아서 리스트로 만들어 봅시다")

xl = [1,2,3,4]

xxl = list(xl)

print(xl, xxl)