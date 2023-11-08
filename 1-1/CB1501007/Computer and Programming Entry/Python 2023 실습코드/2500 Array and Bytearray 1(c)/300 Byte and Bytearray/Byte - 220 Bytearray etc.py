#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-08-31
#-------------------------------------------------------------------------------



values = bytearray([1000,2000,3000])

# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ValueError: byte must be in range(0, 256)
# bytearray에 삽입되는 값은 0~255 범위여야만 한다. 범위 외의 값을 넣으려고 하면 ValueError가 발생


#- 치환

val = b"aaabbb"
val.replace(b"bbb",b"ccc")
print("vals after replacing=", val)


# Buffer protocol은 String과 같은 메소드를 지원한다. String에서처럼 replace()를 사용할 수 있다. 단 argument는 bytes 오브젝트, 즉 “b” 문자열을 사용해야만 함

# - Compare
val1 = b"desktop"
val2 = bytearray(b"desktop")

print(" val1 == val2   ",  val1 == val2)
# 'b' 문자열은 bytes 오브젝트이다. bytes 오브젝트를 비교하려면 ‘==‘를 사용함

# - Start, end

val = b"users"
print(" val.startswith(b'user') = ",   val.startswith(b'user')  )
print("  val.endswith(b's') = ",    val.endswith(b's')  )



# bytes 오브젝트를 string과 같이 다룰 수 있음. startswith와 endswith 역시 사용 가능. 단 argument는 bytes 오브젝트여야만 함
 #- Split, join


data = b"cat,dog,fish,bird"
elem = data.split(b",")

print(" len(elem) = ", len(elem) )

res = b",".join(elem)
print("res=", res )



