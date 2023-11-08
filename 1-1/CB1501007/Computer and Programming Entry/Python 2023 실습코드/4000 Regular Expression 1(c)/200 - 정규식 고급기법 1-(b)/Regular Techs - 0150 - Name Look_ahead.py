

import re


string = "김달수 박도지 김소라 봉달수 제갈달수 감윤탁 여척두 정달수 팽길탄 조척두 박찬욱 봉준호"

print('\n(?=...)=')  # Positive lookahead assertion
print(re.findall(r"(\w+)(?=달수)", string)) # 이름이 달수인 사람의 성



print('\n(?!...) =') # Negative lookahead assertion
print(re.findall(r"(\w+)(?!달수)", string)) # 달수가 아닌 사람들의 성씨



print(' 김씨 성의 이름 뽑아내기') # Positive lookbehind assertion
print(re.findall(r"(?<=김)(\w+\b)", string)) # idn:으로 시작되는 뒷단어
# ['tag', 'tag', 'end']


print('이름이 달수인 사람의 성') # Negative lookbehind assertion
print(re.findall(r"^(?<!:tag)(\b\w*\b)", string)) # idn:으로 시작되지 않는 뒷단어
# ['begin']

