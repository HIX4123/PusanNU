#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-08-31
#-------------------------------------------------------------------------------




values = bytearray([1000,2000,3000])    #  이것울 수행해보자.

# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ValueError: byte must be in range(0, 256)
# bytearray에 삽입되는 값은 0~255 범위여야만 한다. 범위 외의 값을 넣으려고 하면 ValueError가 발생


