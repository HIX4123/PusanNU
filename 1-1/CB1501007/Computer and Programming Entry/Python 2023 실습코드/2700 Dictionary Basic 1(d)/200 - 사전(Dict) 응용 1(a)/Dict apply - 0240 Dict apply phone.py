#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-14
#-------------------------------------------------------------------------------

Pdict={}  # Pdict는 사전구조다.

Pdict["팽길탄"]='010-4323-1899'
Pdict["여척두"]='010-1234-6745'
Pdict["쉰천지"]='04567'
Pdict["이명복"]='NONE'
Pdict["민병훈"]='011-9090-8767'
Pdict["마차돌"]='01-7656-1123'

fname = input("친구이름을 치시요:" )

print( f' 친구{ fname }의 번호는 { Pdict[fname]}')

