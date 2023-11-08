
from operator import itemgetter
data = [('ac', 121),('cac', 231),('bc', 148), ('bc',221), ('ac', 67), ('abx', 9)]

#첫번째 원소로 정렬을 합니다.
alist = sorted(data,key=itemgetter(0))

#두번째 원소로 정렬을 합니다.
blist = sorted(data,key=itemgetter(1))


print(alist)
print(blist)

