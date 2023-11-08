
# ------- set opr ----
sa = { 3, 4, 5, 6, 6, 6, 6, 7}
print(sa)

print(min(sa), max(sa))

t = 3
sa = sa - {t}
print(sa)
sa = sa.union( {t*t} )  # sa = sa + {t} 는 안됨.
print(sa)
# -----------------