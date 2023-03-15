
S=tuple("Is there a ultra-fast W computer in our dept.?")

print(f"Slicing, S[2:6]={S[2:6]}")

nt= S[0:3] + S[-3:-1]
print(f"nt = {nt}")


print(f"공백의 수 = {S.count(' ')}")

try :
    pos = S.index("$")
    print("Element $ Found at : " , pos)
except ValueError as e:
    print(e)


try :
    pos = S.index("W")
    print("Element 'W' Found at : " , pos)
except ValueError as e:
    print(e)