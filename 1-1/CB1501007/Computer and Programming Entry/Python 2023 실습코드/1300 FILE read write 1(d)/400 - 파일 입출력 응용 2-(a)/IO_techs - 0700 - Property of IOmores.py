# 파일입출력 응용을 배웁니다.

# Open and write()
fo = open("foo.txt", "w")
print("1. Name of the file: ", fo.name)
print("2. Closed or not : ",   fo.closed)
print("3. Opening mode : ",    fo.mode)
fo.write( "Python is a great language.");
fo.close()

# Open a file
fo = open("foo.txt", "r+") # Opens a file for both reading and writing.
str = fo.read(10);
print("5. Read String is : ", str)
fo.close()

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print("6. Read String is : ", str)

# Check current position
position = fo.tell();
print("7. Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print("8. Again read String is : ", str)
fo.close()

