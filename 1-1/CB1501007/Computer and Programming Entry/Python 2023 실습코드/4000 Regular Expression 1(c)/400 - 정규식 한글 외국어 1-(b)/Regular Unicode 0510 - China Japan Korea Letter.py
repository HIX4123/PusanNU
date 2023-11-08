

import re

kanji = '漢字'
hiragana = 'ひらがな'
katakana = 'カタカナ'
str = kanji + hiragana + katakana


#Match Kanji
regex = '[\u4E00-\u9FFF]+' # == u'[一-龠々]+'
match = re.search(regex, str, re.U)
print(match.group()) #=> 漢字

#Match Hiragana
regex = '[\u3040-\u309Fー]+' # == u'[ぁ-んー]+'
match = re.search(regex, str, re.U)
print(match.group()) #=> ひらがな

#Match Katakana
regex = '[\u30A0-\u30FF]+' # == u'[ァ-ヾ]+'
match = re.search(regex, str, re.U)
print(match.group()) #=>カタカナ