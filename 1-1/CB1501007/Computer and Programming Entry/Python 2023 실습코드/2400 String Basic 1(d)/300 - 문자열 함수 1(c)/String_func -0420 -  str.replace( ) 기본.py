
# a.upper() →   문자열 a를 모두 대문자로 바꾸어 준다.
# a.lower() →   문자열 a를 모두 소문자로 바꾸어 준다.
# a.swapcase() → 문자열 a의 대문자는 소문자로, 소문자는 대문자로 각각 바꾸어 준다.
# a.count(x) →  문자열 a 중 문자 x와 일치하는 것의 개수를 반환
#               (※ 이때 x는 문자 한 개 일수도, 문자열 일 수도 있다.)
# a.find(x) →   문자열 a 중 문자 x가 처음으로 나온 위치를 반환한다. 없으면 '-1'을 반환
# a.index(x) →  문자열 a 중 문자 x가 처음으로 나온 위치를 반환한다. 없으면 에러를 발생시킨다.
# a.join(s) →   s라는 문자열의 각각의 요소 문자 사이에 문자열 a를 삽입한다.

# 실험1 - 문자열 찾아보기
import string

dna = "AAAGTCCGCTAAAGCATTCGAAATGCA"
other ="ooooooxoooooxoxo"

print("\n string의 문자교체하기 실험")
print(dna.replace("G", "g"))
print(dna)

dna2 = dna.replace("T", "---") #replace 결과값이 저장되는 위치는?
print(dna2)
print(dna)



# 실험 2 - 문자열 대체하기
text = "i love programming so much. But you hate it"
print(text)
print(text.replace('love', 'kill'))



