
#Tkinter -- Canvas의 사용법을 배웁니다. (두개의 공의 rotations)

from tkinter import *
from tkinter.colorchooser import askcolor

(rgb, hx) = askcolor()  # 사용자가 선택한 색상을 돌려준다.

print("당신이 선택한 색의 RGB값은 ", rgb)
print("당신이 선택한 색의 Hexa Code ", hx)
mainloop()
