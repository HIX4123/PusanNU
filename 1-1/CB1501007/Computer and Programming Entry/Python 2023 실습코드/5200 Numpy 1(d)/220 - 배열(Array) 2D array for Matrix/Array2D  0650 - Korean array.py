
from array import array

a = array("i", [10, 20, 30]) # Create an int array of three elements.


print(" array('i', [10, 20, 30]) ") # Display elements in array.
for value in a:
    print((value), end=' ')



a = array("u", "한글처리") # Create a Unicode char array.


print("한글 배열의 출력") # Display letters in array.
for letter in a:
    print(letter)

s = "".join(a.tolist())  # 한 문자로 합치기
print(s)

