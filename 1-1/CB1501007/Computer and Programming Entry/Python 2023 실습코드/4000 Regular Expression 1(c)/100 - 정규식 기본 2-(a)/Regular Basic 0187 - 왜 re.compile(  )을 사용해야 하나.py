

import re

string = "Once you have accom  plished small --+ 567\
          apple good th뭔가요 ings, Yyou mAy atte똥mpt safely.\
          (Summer) time beerXOXtime (Killer) Good Cinema?"

pat1 = r"\b[aeAE][\w]*"      # 'aAeE'로 시작되는 모든 단어를 찾는다.
pat2 = r"\b[A-Z][\w]*"       # 대문자 시작단어
pat3 = r"\w+[A-Z]+\w*"       # 중간에 대문자가 있는 경우

com1  = re.compile( pat1 )      # 'aAeE'로 시작되는 모든 단어를 찾는다.
com2  = re.compile( pat2 )      # 대문자 시작단어
com3  = re.compile( pat3 )      # 중간에 대문자가 있는 경우
com12 = re.compile( '|'.join([pat1,pat2]))
com13 = re.compile( '|'.join([pat1,pat3]))

out1  =  re.findall( com1  , string)
out2  =  re.findall( com2  , string)
out3  =  re.findall( com3  , string)
out12 =  re.findall( com12 , string)
out13 =  re.findall( com13 , string)

print(out1)
print(out2)
print(out3)
print(out12)
print(out13)


