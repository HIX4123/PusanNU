
import os
import glob
import shutil

cwd = os.getcwd()
print("path=", cwd)

test = os.listdir(cwd)
pyc = 0

for item in test:
    if item.endswith(".py"):
        print("I found *.py = ", item)
        pyc += 1
        #os.remove(os.path.join(cwd, item))  # 지울 때 부르면 됨.


print("전체 Python file의 수는 ", pyc)