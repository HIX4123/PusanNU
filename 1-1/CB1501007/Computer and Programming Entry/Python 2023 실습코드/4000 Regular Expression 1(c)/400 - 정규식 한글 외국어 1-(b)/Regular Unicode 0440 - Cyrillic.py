

# hwp에서 바꾼 한자를 넣어서 실험을 함.
# Unicode/0E00-0E7F - Thai — Unicode Character Table 태국
# Cyrillic Range: 0400–04FF The Unicode Standard
# 모든 한자의 범위 [\u4e00-\u9fff]

import re

text1 = """
This page gathers together basic information about the
Cyrillic script and its use человек должен for the Russian language.
It aims (generally) to provide an overview of the
orthography and typographic features, and (specifically) to advise how to write Russian using Unicode; for greater details follow the footnote links (especially those with an arrow alongside them).
 우하하 이것이 러시아 문자이다.
 пола, языка, религии, summer books
"""


for n in re.findall(r'[\u0400-\u04FF]+', text1):
    print(n)