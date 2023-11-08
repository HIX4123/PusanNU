
from tkinter import *

mywin = Tk( )

def hello(event):
    print("한번 Single Click, Button-l")

def hello2(event):
    print("오른쪽 클릭을 하시네요, Button-3")

def hello3(event):
    print("한글 버튼을 클릭했습니다. ")

def quit(event):
    print("두번 Double Click Double-1. 이제  끝냅니다. ")
    import sys; sys.exit()

widget = Button( mywin, text='Mouse Clicks')
widget.pack()
widget2 = Button( mywin, text= '여기도 클릭', bg="green")
widget2.pack()

widget.bind('<Button-1>', hello )
widget.bind('<Button-3>', hello2)  # 오른쪽 클린
widget.bind('<Double-1>', quit  )

widget2.bind('<Button-1>', hello3 )

widget.mainloop()

