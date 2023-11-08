
# match ()    문자열의 처음에서 RE가 일치하는지 결정한다.
# search()    문자열을 훓어서, RE가 일치하는 위치를 찾는다.
# findall()   일치하는 곳의 모든 하부문자열을 찾아서,
#             그 문자열들을 리스트로 반환한다.

# finditer()  일치하는 곳의 모든 하부문자열을 찾아서,
#             그 문자열들을 반복자로 반환한다.

# match()와 search()는 아무 일치도 발견하지 못하면 None을 반환한다.
# 성공적으로 발견하면
# MatchObject 실체가 반환되는데, 여기에는 그 일치에 관한 정보가 담겨 있다:
# 어디에서 시작하고 끝나는지, 일치된 하부문자열, 등등.

# ^Python Match "Python" at the start of a string or internal line
# $Python$  Match "Python" at the end of a string or line
# \APython  Match "Python" at the start of a string
# Python\Z Match "Python" at the end of a string
# \bPython\b Match "Python" at a word boundary
# \brub\B \B is nonword boundary: match "rub" in "rube" and "ruby" but not alone
# Python(?=!) Match "Python", if followed by an exclamation point.
# Python(?!!) Match "Python", if not followed by an exclamation point.

text='''
I forgot to post this column up last year Python!.
It’s a fun one: the Department for Communities and Local
PythonGovernment have producedPython a truly farcical piece of evidence,
and promoted it very hard,
claiming it as good stats.
I noticed the Pythoncolumn was missing today,
because Private Eye have publishedPython on the same report
Pythonin their PythonPython current issue, Python
finding emails that have gone missing through FOI applications,
and other nonsense. That part is all neatly summarised
online in the Local
'''

print (text)