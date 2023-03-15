
S=tuple("이것은 아름다운 부산대학교 컴공의 전통")
print(S)

print(f"Slicing, S[2:6]={S[2:6]}")

nt= S[0:3] + S[-3:-1]
print(f"nt = {nt}")
print(f"S.index = { S.index('부')}" )