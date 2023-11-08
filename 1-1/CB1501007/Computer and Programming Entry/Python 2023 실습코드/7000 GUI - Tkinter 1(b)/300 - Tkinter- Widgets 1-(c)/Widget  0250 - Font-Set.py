
from tkinter import *

# 폰트는 제어판 글꼴에서 이름을 선택할 수 있다.

root = Tk()         # create a Tk root widget

ta = "Hello ! \n 부산대학교 \n Tkinter! \n 열심히 해 봅시다."
tb = "준비가 되었습니까 ? "


msg1 = Label(root, text= ta,  font = ( "맑은 고딕", 20), bg="white" )
msg2 = Label(root, text= tb,  font = ( "맑은 고딕", 30), fg="blue" )

msg1.pack()            # The pack : Tk to fit the size of the window to the given text.
msg2.pack()

root.mainloop()
