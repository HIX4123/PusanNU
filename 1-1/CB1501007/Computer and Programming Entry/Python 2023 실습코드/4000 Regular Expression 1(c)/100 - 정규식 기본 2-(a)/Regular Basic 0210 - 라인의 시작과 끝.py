#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-07-06
#-------------------------------------------------------------------------------

# Various flags used in Python includes
#
#
# Syntax for Regex Flags  What does this flag do
# [re.M] Make begin/end consider each line
# [re.I] It ignores case
# [re.S] Make [ . ]
# [re.U] Make { \w,\W,\b,\B} follows Unicode rules
# [re.L] Make {\w,\W,\b,\B} follow locale
# [re.X] Allow comment in Regex


import re
text2 = "summer wine 다람쥐  corona 코로나 미워요 selenium bababa \
        tomato sogum 오늘 \
        수업은 summer 끝임니다요"

text = """summer
wine 다람쥐  corona
코로나 미워요
selenium bababa \n
tomato sogum
오늘 수업은 끝임니다요"""

out = re.findall(r"^\w+", text) # ^은 줄의 시작
print("\n 1--------", out, )

out = re.findall(r"\w+$", text)
print("\n 2--------", out )

out = re.findall(r"\w+", text)
print("\n 3--------", out, )

out = re.findall(r"^\w+", text, re.M)
print("\n 4--------", out)

out = re.findall(r"\w+$", text, re.M)
print( "\n 5--------", out )






