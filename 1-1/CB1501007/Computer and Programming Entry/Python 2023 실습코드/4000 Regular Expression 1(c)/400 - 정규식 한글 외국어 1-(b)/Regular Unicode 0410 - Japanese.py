
# 파이썬 정규식 한글처리 관련
# 한글 코드 범위
# ㄱ ~ ㅎ: 0x3131 ~ 0x314e
# ㅏ ~ ㅣ: 0x314f ~ 0x3163
# 가 ~ 힣: 0xac00 ~ 0xd79f

import re

text1 = """
test content☆漢字〓韓國外交部對外稱, 應美方要求，
韓國貿易部長金宗塤和美國貿易代表施瓦布本週一
下午還?行了一個「非正式磋商」。end◆
日語〓慰謝料としてフルハウス(Full House)
え ぉ お か が き ぎ くぐけげこごさ ざ し じ す ず せ
をあげるというィヨンジェの言葉に,ジウンは?ても?る事ができないで?む。end
◆ 한글〓해쉬(Hash)값 필터링 시스템(Filtering system)은 디지털 파일에 고유의
키 값을 매겨서 등록, 관리하는 것으로 저작권 침해 신고가 접수됐을 경우
이 키 값을 기준으로 검색, 침해 여부를 판단할 수 있는
방식이다. end★
"""

text2 = """
康京和外相は9日、慰安婦問題をめぐる日韓政府間合意について記
者会見し、合意に基づき日本政府が
拠出した10億円について、韓国政府が予算で負担する
考えを表明した。(時事通信)
"""

# 3040-309F : hiragana
# 30A0-30FF : katakana

regjap = r'[\u3040-\u309F\u30A0-\u30FF]+'

jap = re.compile( regjap ) #  히라가나

a = jap.findall(text1)
for (i, word) in enumerate(a) :
    print(f'i={i:2}, word={word}')

a = jap.findall(text2)
for word in a :
    print(f'i={i:2}, word={word}')



# 한글의 unicode를 출력하려면
# Console에서 다음과 같이 하면 된다.
# >> u'똥'
# >> u'대한민국'
