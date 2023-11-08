# !/usr/bin/python3

import tkinter

root = tkinter.Tk()
# column 0 - do not expand
# column 1 - expand
# root.columnconfigure(0, weight=0)

root.columnconfigure(1, weight=1)
root.rowconfigure   (1, weight=1)

# label / entry pair
l1 = tkinter.Label(root, text="First Name:")
e1 = tkinter.Entry(root)
l1.grid(row=0, column=0, sticky="e")
e1.grid(row=0, column=1, sticky="news")

# label / entry pair
l2 = tkinter.Label(root, text="Last Name:")
e2 = tkinter.Entry(root)
l2.grid(row=1, column=0, sticky="e")
e2.grid(row=1, column=1, sticky="news")

# label / entry pair
l3 = tkinter.Label(root, text="Age:")
e3 = tkinter.Entry(root)
l3.grid(row=2, column=0, sticky="e")
e3.grid(row=2, column=1, sticky="news")



root.mainloop()



