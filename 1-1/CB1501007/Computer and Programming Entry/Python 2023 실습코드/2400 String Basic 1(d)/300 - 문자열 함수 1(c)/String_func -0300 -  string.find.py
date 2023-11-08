


str1 = "어디로 가야하는가 어데로 가야하는가 이말이다. 산으로 가나? 바다로 가야 ? ";
str2 = "가야";

print( "lenth(str1)=", len(str1) )
print("Out a =", str1.find(str2))
print("Out b =", str1.find(str2, 10))  # 범위는 10이상 부터
print("Out b =", str1.find(str2, 15,19))  # 범위는 10이상 부터
print("Out c =", str1.find(str2, 30))
print("Out d =", str1.find(str2, 40))

# rfind() returns the last index where the substring str is found,
# or -1 if no such index exists, optionally restricting the search to
# string[beg:end].
print("\n\n rfind( ) 사용하기")

print("Out1 =", str1.rfind(str2))

print("Out2 =", str1.rfind(str2, 0, 10))  #
print("Out3 =", str1.rfind(str2, 10, 0))

print("Out4 =", str1.find(str2))
print("Out5 =", str1.find(str2, 0, 10))
print("Out6 =", str1.find(str2, 10, 0))
