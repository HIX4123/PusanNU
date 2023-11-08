

la = [ 10, 76, 134, 23, 6, 7, 12, 9, 33, 56, 1, 4, 5, 60]
print(la)

lb = sorted(la[0:5])
print(lb)
la[0:5] = sorted(la[0:5],reverse=True)
print(la)


import operator  # 두번째 원소를 중심으로 sorting

l = [[1,4,3], [2,2,4], [3,1,5], [0,9], [111,3,-2]]
print("Using Operator=", sorted(l, key=operator.itemgetter(1)))