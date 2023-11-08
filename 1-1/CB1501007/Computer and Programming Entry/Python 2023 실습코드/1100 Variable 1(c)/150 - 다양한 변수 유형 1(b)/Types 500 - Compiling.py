

# 프로그램을 compile하여 pyc를 만드는 방법
# python -m a.py

# 특정 디렉토리 아래에 있는
# python -m compileall .
C = """

import py_compile

py_compile.compile("file.py") #compiles single file named file.py


2.python -m compileall ./ #combines all programs under current directory


Both approaches work in Python2 and Python3. Only difference in Python2 and Python3 is:

1.Python2 generates .pyc file in the same directory whereas


2.Python3 creates it in a folder named __pycache__ inside the same directory.

"""


a = 100
b = 1000
print((a + b))

if a < b :
    print("a <  b")
else :
    print("a >= b")