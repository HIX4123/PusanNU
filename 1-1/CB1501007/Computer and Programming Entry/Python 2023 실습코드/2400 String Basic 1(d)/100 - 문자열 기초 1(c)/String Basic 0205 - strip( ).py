
# string을 다양하게 분리해 본다.
# 어절을 잘라내는 기능을 한다.
# a.strip() →   문자열 a의 양쪽 공백을 모두 지운다.
# a.lstrip() →  문자열 a의 왼쪽 공백을 모두 지운다.
# a.rstrip() →  문자열 a의 오른쪽 공백을 모두 지운다.
# a.replace(s, r) → 문자열 a의 s라는 문자열을 r이라는 문자열로 치환한다.
# a.split(s) →  문자열 a를 s를 구분자로 하여 나누어 준다. a.split()은 공백을 기준으로 한다. 이때 s는 제외된다.



print("\n Experiment 1")
mystr="   apple  banana cola      "
print("[",mystr,"]")
print("[",mystr.lstrip(),"]")
print("[",mystr.rstrip(),"]")
print("[",mystr.strip(),"]")
print(mystr.swapcase())

print("\n Experiment 2")
mystr = "0001000100372821%%%%9999+++++"
print(mystr.lstrip("0"))
print(mystr.rstrip("+"))
print(mystr.lstrip("0001"))
print(mystr.rstrip("+9%"))

print("\n Experiment 3")
mystr = "   Jan   Feb  March  April May  June    "
chostr = " CHO ;  51 ;  man ; Computer Science ; ; drink"
boystr = " CHO2 ;  11 ;  man ; Elementary  ; TV ; ; "
print(mystr.split())
info = chostr.split(";")
print(info)

print("\n Experiment 4")
print("  a ; b ; c ; d  e".rsplit(';',2))
print("  a ; b ; c ; d  e".split (';',2))
print("  a ; b ; c ; d  e".rsplit(';',3))
print("  a ; b ; c ; d  e".split (' ',3))
multilines= "this \n is a sample statemnt \n in our \n department store"
print(multilines)
print(multilines.splitlines())

print("\n Experiment 5")
print("234".zfill(10))
print("456234".zfill(10))
print("23490".zfill(20))
print("mybook.txt".endswith("txt"))
print("mybook.txt".startswith("txt"))


