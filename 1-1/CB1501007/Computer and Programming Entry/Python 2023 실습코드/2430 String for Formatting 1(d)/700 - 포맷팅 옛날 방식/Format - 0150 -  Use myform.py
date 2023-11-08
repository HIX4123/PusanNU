#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

lst1="""
    More than 3,000 years ago, ancient Egypt, with its myriad gods
    and goddesses, saw the founding of two monotheistic religions within
    a century of each other. One is associated with Moses,
    the Bible and ancient Israel’s faith, which is the foundation of
    Judaism and Christianity. The other burst on to the scene around
    1350 BCE, flourished for a moment, and was then eclipsed when
    its founder died in 1336 BCE.""".split()

lst2="""
아산의 부모는 이집트 군부독재 정권의 박해를 피해 2017년
한국으로 온 ‘난민신청자’다. 모나 부부는 2021년 새해
첫날 태어난 아산에게만큼은 난민신청자 신분을 물려주고
싶지 않았지만, 달리 방도가 없었다. 본국에서 박해를 피해
한국으로 망명한 터라 주한 이집트 대사관을 찾아 출생신고를
할 수도 없었고, 한국에서 출생신고를 할 수도 없었다.
미등록체류’ 상태로 석달을 살았던 아산은 난민신청서를
낸 뒤에야 외국인등록증을 손에 쥘 수 있었다.
보통 아동들이 생후 1∼2개월에 맞는 예방접종 주사도 아산은
외국인등록증을 받은 뒤에야 맞을 수 있었다.
""".split()

# 원문보기:
# https://www.hani.co.kr/arti/society/society_general/994035.html?_fr=mt2#csidx207c270bd1dfb02a86962064cd1b093 .""".split()

lst1.sort()


for i, w in enumerate(lst1) :
    out = f"i={i:>6}  string= {w:<15}"
    print( out )

for i, w in enumerate(lst2) :
    out = f"i={i:>6}  string= {w:<15}"
    print( out )


# {:>nd} 숫자를 오른쪽으로 정렬한다. 최대 길이는 n 자리
# {:<ns} 문자를 왼쪽으로 정렬한다. 최대 길이는 n 자리