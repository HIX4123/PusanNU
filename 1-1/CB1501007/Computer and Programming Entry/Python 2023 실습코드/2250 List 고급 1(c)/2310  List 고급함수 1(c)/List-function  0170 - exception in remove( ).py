
a= [11, 33, 4, 9, 87, 66, 55, 11, 33 ]

#a.remove( 77 ) # this does not work
# 따라서 당신은 반드시
c = 77
if c in a:
    a.remove(c)

# or:
try:
    a.remove(c)
except ValueError:
    print("없는 원소를 remove( ) 해서는 안됩니다")
    pass

print("실험이 끝났습니다. ")


# 값이 아니고 특정번째 원소를 지우려고 한다면

print(a.index(87))
#print a.index(-87) # 이러면 오류가 납니다.