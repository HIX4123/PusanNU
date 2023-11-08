
from tkinter import *
root=Tk()
root.title(" 캔버스에 스크롤달기")

frame=Frame(root,width=300,height=300)
frame.grid(row=0,column=0)
Myfont =  ( "맑은 고딕", 20)

canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))

canvas.create_text( 100, 150, font=Myfont, fill="blue", text='이것이 무엇이냐')
##b1 = Button(root, text="Foo")
##b1.place(x=110,y= 120)


hbar=Scrollbar (frame, orient=HORIZONTAL)
hbar.pack      (side=BOTTOM,fill=X)
hbar.config    (command=canvas.xview)

vbar=Scrollbar (frame, orient=VERTICAL)
vbar.pack      (side=RIGHT,fill=Y)
vbar.config    (command=canvas.yview)

canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack( side=LEFT, expand=True, fill=BOTH)

root.mainloop()