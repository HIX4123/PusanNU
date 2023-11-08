num = int(open(0).readline())

req = [tuple(map(int, open(0).readline().split())) for i in range(int(num))]

res = [0] * num

for idx, val in enumerate(req):
    for j in req:
        if val[0] <= j[0] and val[1] <= j[1]:
            res[idx] += 1

print(*res)