
from tkinter import *

def on_enter(event):
    widget = event.widget
    print("\n Input=>>> ", (widget.get()))
    widget.delete(0, "end")

root = Tk()
parent = Frame(root)
parent.grid()
mylabel = Label(text="What you know:", bg="yellow")
mylabel.grid()



#Entry.bind('<Return>', on_enter)
myentry = Entry(parent, show="*") #shows each character as an asterix
#myentry = Entry(parent )
myentry.grid()
myentry.bind('<Return>', on_enter)


root.mainloop()