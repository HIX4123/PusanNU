
unicode_a ='\N{LATIN SMALL LETTER A}'
print(unicode_a)
unicode_a_with_acute = '\N{LATIN SMALL LETTER A WITH ACUTE}'
print(unicode_a_with_acute)
mychar = "\u00E1"
print(mychar)

print("실험 2 ------------- ", 'a\n\tb')
print("abc\n")

print("실험 3 ---------------")
a = 450 ; b = -9843 ; c = -13.456
d = 98  ; e = 3728190 ; f = 0.4567
print("%d, %d, %d" % (a,b,c))    # %d : 10진 정수
print("%d, %d, %d" % (d,e,f))

print("실험 4 ---------------")
print("%10d, %10d, %10d" % (a,b,c))
print("%10d, %10d, %10d" % (d,e,f))

print("\n 16진수와 8진수")
print("%x, %x, %x" % (a,b,c))    # %x : 16진수
print("%o, %o, %o" % (a,b,c))    # %o " 8진수

print("\n실험 5 ---------------")
print("%f, %d, %e" % (-247.78934,10.00982,150.736453))   # %e : 부동 소수점(실수)를 지수 형태로 표현,
                                                        # 유효 숫자는 7자리로 표현한다.
print("%10.2f, %d, %e" % (-247.78934,10.00982,150.736453))
print("%10.2f, %10.5d, %10.1f" % (-247.78934,10.00982,150.736453))
print("%s, %c, %x" % (100,100,100))  # %c : 길이 1의 문자
print("%c, %c, %c" % (100,110,115))

print("\n실험 6 ---------------")
nums = [ 345, -9, -90839, 782.090, 87, 768392934, -0.234, -98372, 23, 45]
for x in nums :
    print(" num = %d " % x)

print("\n실험 7 ---------------")
for x in nums :
    print(" num = %+10d "% x)