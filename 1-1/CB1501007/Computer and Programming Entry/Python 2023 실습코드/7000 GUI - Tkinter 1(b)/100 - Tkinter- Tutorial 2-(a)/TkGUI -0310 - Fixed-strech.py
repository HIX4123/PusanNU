
import tkinter

root = tkinter.Tk()

# label / entry pair
l1 = tkinter.Label(root, text=u"이름:")
e1 = tkinter.Entry(root)

# put in first row
l1.grid(row=0, column=0, sticky="e")
e1.grid(row=0, column=1)

# label / entry pair
l2 = tkinter.Label(root, text="Last Name:")
e2 = tkinter.Entry(root)

# put in first row
l2.grid(row=1, column=0, sticky="e")
e2.grid(row=1, column=1)

# label / entry pair
l3 = tkinter.Label(root, text="Age:")
e3 = tkinter.Entry(root)

# put in first row
l3.grid(row=2, column=0, sticky="e")
e3.grid(row=2, column=1)

# column 0 - 그대로 머물어 있도록 한다. Weight=0
root.columnconfigure(0, weight=0)

# column 1 - Strech하면 그대로 늘어나도록 한다. weight=1
root.columnconfigure(1, weight=1)

root.mainloop()


