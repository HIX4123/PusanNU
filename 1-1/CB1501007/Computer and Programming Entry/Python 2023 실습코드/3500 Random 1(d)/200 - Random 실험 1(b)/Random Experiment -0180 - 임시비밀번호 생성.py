# string.ascii_lowercase¶
# string.ascii_letters
# string.ascii_lowercase
# The lowercase letters 'abcdefghijklmnopqrstuvwxyz'.
# string.ascii_uppercase
# The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
# string.digits, The string '0123456789'.
# string.hexdigits, The string '0123456789abcdefABCDEF'.
# string.octdigits, The string '01234567'.
# string.punctuation, in the C locale.
# string.printable
# string.whitespace


import string
import random   # for random
random.seed()   # 씨앗(seed)값 설정하기. 시간 정보에 의해 초기화됨


print(string.digits)
print(string.ascii_lowercase)

def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

s=string.ascii_lowercase+string.digits
''.join(random.sample(s,10))

print("랜덤1 word =", randomword(12))

s="computer systems class"
for x in range(10):
    print(random.sample(s,5))


t=[0, 99, 33, 23, 45, 5, 6, 77, 100, 23, 55, -34, -9]

print(random.sample(t, 6))