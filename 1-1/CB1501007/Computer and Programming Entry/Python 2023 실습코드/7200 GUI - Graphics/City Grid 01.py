

from tkinter import *

def on_enter(event):
    widget = event.widget
    myid = widget.get()
    print("Moving Direction=", myid,"\n 길이는 = ", len(myid))
    e1.delete(0,END)  # 화면에 입력된 것을 지움

W = 1000
H = 600

master = Tk()

mypaper = Canvas(master, width= W, height=H )
mypaper.pack()

Label(master, text= "Cop Move").place(x=800, y=100)


e1 = Entry(master)
e1.focus_set()            # 입력 커서를 이쪽으로  이것이 없으면 커서는 아무데나
#e1.insert(5, " ")
e1.place(x=830, y=100)
e1.bind('<Return>', on_enter)

xgap = 100
csize = 50
leftx = 100
lefty = 100
for q in range(5):
    for w in range(7):
        mypaper.create_oval( leftx, lefty, leftx+csize, lefty+csize, width=2, fill="orange")
        leftx += xgap
    lefty += xgap
    leftx = 100


mainloop()
