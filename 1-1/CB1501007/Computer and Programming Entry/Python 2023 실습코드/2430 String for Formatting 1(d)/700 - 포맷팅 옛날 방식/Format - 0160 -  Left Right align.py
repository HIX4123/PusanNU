#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

lst="""
    More than 3,000 years ago, ancient Egypt, with its myriad gods
    and goddesses, saw the founding of two monotheistic religions within
    a century of each other. One is associated with Moses,
    the Bible and ancient Israel’s faith, which is the foundation of
    Judaism and Christianity. The other burst on to the scene around
    1350 BCE, flourished for a moment, and was then eclipsed when
    its founder died in 1336 BCE.""".split()

lst.sort()

for i, w in enumerate(lst) :
    out = f"{i:>6}  {w:<15}"
    print( out )


# {:>nd} 숫자를 오른쪽으로 정렬한다. 최대 길이는 n 자리
# {:<ns} 문자를 왼쪽으로 정렬한다. 최대 길이는 n 자리