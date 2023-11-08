
import string  # 문자열에 대한 특별한 처리를 위해서 import 함

print("실험 1. 집합")

cozy = 345.6728

a = { 1, 2, 3, "star craft", "what did you?", cozy , 45e-5 }
print("집합 a를 출력합니다", a)


SampleString = "To be or not to be. Be is not to be Bee. To is not Two"
occurrences = {}
Slist = string.split(SampleString) # 어절별로 잘라서 리스트를 만듬

for word in Slist :
	occurrences[word] = occurrences.get(word, 0) + 1

for word in list(occurrences.keys()):
	print("The word [", word, "] occurs", occurrences[word], \
              "time(s) in the string")
