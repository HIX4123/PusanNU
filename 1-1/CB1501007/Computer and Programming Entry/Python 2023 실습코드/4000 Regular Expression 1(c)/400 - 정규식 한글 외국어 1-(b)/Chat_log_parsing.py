#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-06-22
#-------------------------------------------------------------------------------

import re

chat="""
#Chat No.00063 user: "백광익" time: 0:06
- 채팅10만돌파하겟네
#Chat No.00064 user: "hyemi hong" time: 0:06
- 뭐여 ㅋㅋㅋㅋ
#Chat No.00065 user: "cehe kim" time: 0:06
- 시작
#Chat No.00066 user: "YoungHoon KIM" time: 0:06
- 공장장을 지키기위해 우리가 할 수 있는 일 : 공장장을 징계하려는 방심위 허미숙, 윤정주를 추천한 배후를 찾아서 그들을 민주당 경선에서 탈락시켜야한다.민주당 권리당원에 가입합시다. 허미숙은 정세균 추천, 윤정주는 민주당 폐미계가 추천했다고 합니다.
#Chat No.00067 user: "RAINY" time: 0:07
- 7
#Chat No.00068 user: "아이작." time: 0:07
- 와우 채팅 창 장난 아니네
#Chat No.00069 user: "권은경" time: 0:07
- 딴지마켓구입=김어준후원
#Chat No.00070 user: "온종일뛴다" time: 0:07
- 댓읽기 딱 맞춰서 끝내주네 ㄷㄷ
#Chat No.00071 user: "하얀이마을" time: 0:08
- 이 시간 너무 좋아
#Chat No.00072 user: "dalsong" time: 0:08
- 3
#Chat No.00073 user: "유지연" time: 0:08
- 십만?
#Chat No.00074 user: "김진영" time: 0:09
- 좋아요 안누른사람
#Chat No.00075 user: "어른아이" time: 0:09
- 이 bgm 뭐약 ㅋㅋ
#Chat No.00076 user: "SK S" time: 0:09
- 우리 세대에서 반민족행위자 처벌이 이루어 졌으면 좋겠다
#Chat No.00077 user: "J.K Yoo" time: 0:09
- 김어준 보유국!
#Chat No.00078 user: "김선영" time: 0:10
- 기대됩니다
#Chat No.00079 user: "리에박" time: 0:10
- 시작
#Chat No.00080 user: "이쁜교량사진관-유튜브" time: 0:10
- ??????????
#Chat No.00081 user: "Lee이슬처럼" time: 0:10
- 총수님 나오신다
#Chat No.00082 user: "백오드리" time: 0:11
- 가즈아~~
#Chat No.00083 user: "정태경" time: 0:11
- 좋아요 한표 투척^^
#Chat No.00084 user: "IlWoo-RooT Kim" time: 0:11
- 털본 나올까?
#Chat No.00085 user: "Clara" time: 0:12
- @리에박 님??????
#Chat No.00086 user: "미카" time: 0:12
- 좋아요 눌러주세요~ 좋아요는 사랑입니다~♥?
#Chat No.00087 user: "이승용" time: 0:12
- 조정하고 광고 나오믄;;;
#Chat No.00088 user: "바람소리" time: 0:12
- 멋지네
#Chat No.00089 user: "박일라" time: 0:13
- 고고고
#Chat No.00090 user: "정명아" time: 0:13
- 금요일 다스봐야 한 주 마감됨ㅋ
#Chat No.00091 user: "김담이" time: 0:13
- ????????????????????????????????????
#Chat No.00092 user: "뽀글뽀글" time: 0:13
- 몇명모였다고 벌써 버퍼
#Chat No.00093 user: "백승원" time: 0:14
- 시작!!
#Chat No.00094 user: "해피타임" time: 0:14
- 주진우기자 화이팅~♡♡
#Chat No.00095 user: "김남수" time: 0:14
- 김어준짱
#Chat No.00096 user: "김라니" time: 0:14
- 우와~~~~~~~~♥
#Chat No.00097 user: "아무르임" time: 0:16
- 오늘도즐거운시간
#Chat No.00098 user: "정재홍" time: 0:16
- 나와
#Chat No.00099 user: "블루래빗" time: 0:16
- 좋아요
#Chat No.00100 user: "한욱주" time: 0:16
- 대한독립만세
#Chat No.00101 user: "봄봄인가" time: 0:17
- 와~~~~~
#Chat No.00102 user: "김미희" time: 0:17
- 우린 설득하는데지쳐서 포기했음
#Chat No.00103 user: "똥달푸" time: 0:17
- 울 아빠트 털보랑 닮은 청년 살아
#Chat No.00104 user: "이상국" time: 0:18
- 어준 도령나와라
#Chat No.00105 user: "1002놀자" time: 0:18
"""

mypat=r"Chat No\.(\d\d\d\d\d) user: \"([가-힝]+)\" time: (\d+:\d+)[\s ]+- ([\w ]+)"

la = re.findall( mypat, chat, re.M|re.I )
for w in la :
    print(w)

mypat=r"- ([\w ]+)"

la = re.findall( mypat, chat, re.M|re.I )
for w in la :
    print(w)
