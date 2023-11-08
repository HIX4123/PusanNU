
#  어떤 pattern앞이나 뒤에 나타나는 특정 token을 찾는다.
# 이 경우 이 시작점을 지정하는 patter에는 *, +와 같은 길이가 고정되지
# 않는 것은 사용할 수 없다.

import re

def print_match(match):
    if match is None:
        print('No match')
        return

    print(match.group())
    return match


string = "begin:id12:tag:id05:tag:id37:end"

print('\n(?=...)=')  # Positive lookahead assertion
print(re.findall(r"(id\d+)(?=:tag)", string)) # :tag을 끝나는 앞단어 idN



print('\n(?!...) =') # Negative lookahead assertion
print(re.findall(r"(id\d+)(?!:tag)", string)) # :tag으로 끝나지 않는 앞단어 idN


# Positive lookbehind assertion 이 경우 앞은 항상 고정형, +나 *는 허용하지 않는다.
print('\n(?<=...)=')
print(re.findall(r"(?<=id\d\d:)(\b\w*\b)", string)) # idn:으로 시작되는 뒷단어
# ['tag', 'tag', 'end']


print('\n(?<!...)=') # Negative lookbehind assertion
print(re.findall(r"^(?<!:tag)(\b\w*\b)", string)) # idn:으로 시작되지 않는 뒷단어
# ['begin']


print('\n(?(id/name)yes-pattern|no-pattern)')
# Will try to match with yes-pattern if the group with given id or name exists,
# and with (optional) no-pattern if it does not.
print_match(re.match("(<)?[^<]*(?(1)>)", "<identifier>text"))
# <identifier>


print_match(re.match("(<)?[^<]*(?(1)>)", "text<identifier>"))
# text
