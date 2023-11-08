
import os.path
import glob

files = glob.glob('*')
for x in files:
     if os.path.isdir(x):             # 디렉터리인가?
         print(('%s <DIR>' % x))
     #else:
     #    print(x)

