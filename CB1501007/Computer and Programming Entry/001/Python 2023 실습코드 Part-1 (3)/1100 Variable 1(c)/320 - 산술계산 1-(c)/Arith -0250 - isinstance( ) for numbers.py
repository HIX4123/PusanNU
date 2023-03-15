#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-09-02
#-------------------------------------------------------------------------------


# file에서 읽으면 항상 string으로 들어온다.

slist=[ 456, '78', 3.456, '0.987', 'summer', '83']

alist=[]
for w in slist :
    print(f' w={w}, type={type(w)}')
    if isinstance(w, int)  :
        w = w + 10
    if isinstance(w, float) :
        w = w + 100.0

    alist.append(w)



print(alist)



