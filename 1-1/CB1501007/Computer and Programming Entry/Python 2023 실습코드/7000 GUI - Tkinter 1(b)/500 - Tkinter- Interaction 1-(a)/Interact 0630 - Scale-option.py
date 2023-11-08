
#-----------------------------------------------------------------------------

from tkinter import *


def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)


root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var, orient=HORIZONTAL, from_=100, to=200, length=200  )
scale.pack(anchor=CENTER)


button = Button(root, text="Get Scale Value", command=sel )
button.pack(anchor=CENTER)


label = Label(root)
label.pack()

root.mainloop()
