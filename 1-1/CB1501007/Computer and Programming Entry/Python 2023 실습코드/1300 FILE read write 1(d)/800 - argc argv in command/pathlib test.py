#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-11-16
#-------------------------------------------------------------------------------


# from pathlib import Path (window에서만 사용가능한 Code)

from pathlib import Path
my_file = Path("C:\\Data\\Python\\기사예제.txt")    # Path는 string을 return하는것 아님.window에서만 사용하능함.
if my_file.is_file():
  print("Yes it is a file")