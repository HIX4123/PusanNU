


str1 = "우리는 아름다운 강산에 살고 있습니다. 아끼고 또 아껴\
아름다운 강산을 자손들에게 잘 물려줍시다, 우리 강산 푸르게 "

str2 = """ 우리는 아름다운 강산에 살고 있습니다.
아끼고 또 아껴
아름다운 강산을 자손들에게 잘 물려줍시다, 우리 강산 푸르게 """

idx = str1.find("강산")
print( str1[idx-3] )


idx = str1.find("강산", 12)
print( str1[idx:idx+5] )