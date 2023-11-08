# 다양한 split delimiter 실험
import re
ktxt="이것은 한글이냐   한글이 아니냐?       34 +  66 은 무엇인가 ? "


out1 = re.split(r' *', ktxt)
print("\n out1=", out1)

out1 = re.split(r' ', ktxt)
print("\n out2=", out1)

print("\n out3=",ktxt.split())