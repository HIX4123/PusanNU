#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-11-16
#-------------------------------------------------------------------------------

import os.path                                         # 메소드 call을 위한 module불러오기
file = 'C:\\Data\\Python\\기사예제.txt'     # 예제 Textfile

if os.path.isfile(file):
  print("Yes. it is a file")
esif os.path.isdir(file):
  print("Yes. it is a directory")
esif os.path.exists(file):
  print("Something exist")
else :
  print("Nothing")