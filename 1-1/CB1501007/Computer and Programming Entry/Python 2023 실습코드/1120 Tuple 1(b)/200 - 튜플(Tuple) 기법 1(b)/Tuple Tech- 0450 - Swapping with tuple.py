
# 튜플이 없을 때
str1 = 'dog'
str2 = 'pig'

print(str1, str2)
temp = str1
str1 = str2
str2 = temp
print(str1, str2)

print("\n Tuple을 이용한 swap")
print(str3, str4)
str3 = 'banana'
str4 = 'tomato'

str3, str4 = str4, str3
#(str3, str4) = (str4, str3)

print(str3, str4)


