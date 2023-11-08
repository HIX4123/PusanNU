
n = 5
xlist = [ [] for _ in range(n)]
print("xlist=", xlist)


ylist = [[]] * 5
print("ylist=", ylist)

ylist[0].append(1)
print("ylist=", ylist)


list1, list2, list3, list4 = ([] for i in range(4))
print(list1, list2, list3, list4)


def mklist(n):
    for _ in range(n):
        yield []


zlist = list(mklist(10))
print("zlist=", zlist)