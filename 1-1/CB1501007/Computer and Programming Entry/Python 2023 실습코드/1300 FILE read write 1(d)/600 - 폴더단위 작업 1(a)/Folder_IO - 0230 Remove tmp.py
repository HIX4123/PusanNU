
import os
import glob
import shutil

cwd = os.getcwd()
print("path=", cwd)

for f in os.listdir(cwd):
    ntmp = os.path.join(cwd, f)
    try:
        print(ntmp)
        # os.remove(ntmp)
    except OSError as errf:
        print
        errf


test = os.listdir(cwd)

for item in test:
    if item.endswith(".txt"):
        print("I found = ", item)
        #os.remove(os.path.join(cwd, item))  # 지울 때 부르면 됨.