
def gen():
    val = 111111
    while True:
        val = (yield val) * 111111

g = gen()

print((next(g)))  # 111111
print((g.send(2)))  # 222222
print((g.send(3)))  # 333333
