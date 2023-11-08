import os
import shutil
shutil.copy2('foo22.txt', 'foo33.txt') # complete target filename given



n = os.path.getsize("foo33.txt")
print(n, "Bytes")                           # 바이트 단위로 구하기
print(n / 1024, "KB")                       # 킬로바이트 단위로
print("%.2f MB" % (n / (1024.0 * 1024.0)))  # 메가바이트 단위로
