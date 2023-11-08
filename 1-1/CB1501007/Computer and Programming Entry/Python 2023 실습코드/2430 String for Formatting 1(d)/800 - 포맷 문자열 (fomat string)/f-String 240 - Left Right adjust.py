#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

lst="""
    More than 3,000 years ago, ancient Egypt, with its myriad gods
    and goddesses,
    the Bible and ancient Israel’s faith, which is the foundation of
    Judaism and Christianity.""".split()

lst.sort()

for i, w in enumerate(lst) :
    out = f'{i:6}  {w:15}'
    print( out )



# {:>nd} 숫자를 오른쪽으로 정렬한다. 최대 길이는 n 자리
# {:<ns} 문자를 왼쪽으로 정렬한다. 최대 길이는 n 자리