x = [
 ['4', '21', '1', '14Gorillar', '15:42:58'],
 ['3', '22', '4', '2somename', '15:22:03'],
 ['5', '21', '3', '19bookbox', '15:45:45'],
 ['6', '21', '1', '1somename', '15:45:49'],
 ['7', '22', '3', '2somename', '15:45:51']
 ]

from operator import itemgetter

x.sort(key=itemgetter(1))

for w in x :
    print(w)


print("\n\n 시간으로 정렬해보기")
x.sort(key=itemgetter(4))

for w in x :
    print(w)
