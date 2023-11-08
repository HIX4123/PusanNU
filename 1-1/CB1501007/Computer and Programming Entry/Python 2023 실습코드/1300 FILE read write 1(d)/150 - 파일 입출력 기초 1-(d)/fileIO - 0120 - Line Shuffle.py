#-------------------------------------------------------------------------------
# Purpose:     Zoh's Work     "過猶不及"
#-------------------------------------------------------------------------------
import random
with open("Seoul.txt",encoding='cp949') as f:
    lines = f.readlines()
random.shuffle(lines)
with open("Seoul_Random.txt", "w",encoding='cp949') as f:
    f.writelines(lines)

f.close()