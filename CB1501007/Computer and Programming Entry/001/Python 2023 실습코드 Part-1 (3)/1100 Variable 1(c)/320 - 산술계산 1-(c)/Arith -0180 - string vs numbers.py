#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-09-02
#-------------------------------------------------------------------------------


# file에서 읽으면 항상 string으로 들어온다.

slist=[ '456', '78', '0.987', 'summer', '83']

alist=[]
for w in slist :
    print(f' w={w}, type={type(w)}')
    if type(w) == type(34) :
        w = int(w)
        alist.append(w)
    if type(w) == type(3.4) :
        w = float(w)
        alist.append(w)



print(alist)



