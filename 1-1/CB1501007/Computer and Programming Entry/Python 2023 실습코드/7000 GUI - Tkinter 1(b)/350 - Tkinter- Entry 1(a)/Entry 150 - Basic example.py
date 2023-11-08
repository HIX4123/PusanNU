

from tkinter import *

top =Tk()
top.geometry("300x400+30+30")  # 크기와 처음 놓는 위
top.title( '연습용 Entry widget')


L1 = Label(top, text= "사용자 이름")
L1.place(x=50, y=125 ) # place grid, pack 을 섞어쓰면 안됨.


E1 = Entry(top, bd =2, bg="lightgreen")
E1.place(x=50, y=150 )

def callback():
    ans = E1.get()
    print("입력된 이름은=", ans)
    if ans == "끝" :
        print("빠이빠이")
        exit()

accept = Button(top, text="OK", width=10, command=callback)
accept.place(x=180, y=150 )


top.mainloop()