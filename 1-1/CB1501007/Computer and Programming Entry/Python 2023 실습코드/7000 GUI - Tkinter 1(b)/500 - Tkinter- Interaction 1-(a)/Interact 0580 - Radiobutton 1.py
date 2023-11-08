
from tkinter import *

def sel():
   selection = "당신이 선택한 Option : " + str(var.get())
   label.config(text = selection, bg="dark red", fg="white")

root = Tk()
root.geometry("300x400+300+300")

var = IntVar()      #공유되는 변수룰 지정한다. variable
var.set(1)          # 특별히 선택되지 않았을 때 default 설정

R1 = Radiobutton(root, text="컴퓨터공학전공",  variable=var, value=1, command=sel)
R2 = Radiobutton(root, text="전기공학전공",    variable=var, value=2, command=sel)
R3 = Radiobutton(root, text="타학과(부전공)",  variable=var, value=3, command=sel)
R1.grid( row=10, column=10 , sticky=W )
R2.grid( row=20, column=10 , sticky=W )
R3.grid( row=30, column=10 , sticky=W )


label = Label(root)
label.grid(row=70, column=20, sticky=E)
root.mainloop()