
from array import array

# Create an int array of three elements.
a = array("i", [10, 20, 30])

# Display elements in array.
print(" array('i', [10, 20, 30]) ")
for value in a:
    print((value), end=' ')


# Create a Unicode char array.
a = array("u", "한글처리")

# Display letters in array.
print("한글 배열의 출력")
for letter in a:
    print(letter)

# Convert array to a list.
# ... Then join it.
s = "".join(a.tolist())
print(s)

