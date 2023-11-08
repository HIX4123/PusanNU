
from tkinter import *

def sel():
   selection = "당신의 준비물 : " + var2.get()
   label.config(text = selection, font=("맑은 고딕", 16),  fg="blue",relief=RIDGE, width=25)

root = Tk()
root.geometry("400x500+100+50")
var2 = StringVar()
var2.set("piano")

                                            #공유되는 변수=variable
R1 = Radiobutton(root, text="미술학과",    variable=var2, value="canvas", command=sel)
R2 = Radiobutton(root, text="음악학과",    variable=var2, value="cello",  command=sel)
R3 = Radiobutton(root, text="무용학과",    variable=var2, value="tow-shose", command=sel)
R1.grid( row=10, column=10 , sticky=W )
R2.grid( row=20, column=10 , sticky=W )
R3.grid( row=30, column=10 , sticky=W )


label = Label(root)
label.grid(row=70, column=10,  sticky=E )
root.mainloop()