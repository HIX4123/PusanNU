
from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
frame1 = Frame(root, borderwidth=2, relief= RAISED, bg="orange")
frame1.pack()

R1 = Radiobutton( frame1, text="Option 1", variable=var, value=1, command=sel)
R1.pack( side=LEFT )

R2 = Radiobutton( frame1, text="Option 2", variable=var, value=2, command=sel)
R2.pack(side=LEFT  )

R3 = Radiobutton( frame1, text="Option 3", variable=var, value=3, command=sel)
R3.pack( side=LEFT  )

label = Label(root, bg="red")
label.pack(  )
root.mainloop()