
from tkinter import *

master = Tk()


listbox = Listbox(master, fg="black", bg="wheat")
listbox.pack()

listbox.insert(END, "a list entry" )

for item in ["1. one", "2. two", "3. three", "4. four"]:
    listbox.insert(END, item)

mainloop()