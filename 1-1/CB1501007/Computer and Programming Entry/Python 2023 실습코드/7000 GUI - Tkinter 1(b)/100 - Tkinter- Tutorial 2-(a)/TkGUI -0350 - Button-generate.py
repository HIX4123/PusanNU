import tkinter

root = tkinter.Tk()

# create and pack containers
top    = tkinter.Frame(root, background= "red")
bottom = tkinter.Frame(root, background="blue")
top.pack(fill="x")
bottom.pack(expand="yes", fill="both")

# just use pack on buttons on top
b1 = tkinter.Button(top, text="Foo")
b2 = tkinter.Button(top, text="Bar")
b3 = tkinter.Button(top, text="Baz")
b1.pack(side="left", expand="yes", fill="x", padx=5, pady=5)
b2.pack(side="left", expand="yes", fill="x", padx=5, pady=5)
b3.pack(side="left", expand="yes", fill="x", padx=5, pady=5)

# use grid on the bottom
for x in range(4):
    for y in range(4):
        b = tkinter.Button(bottom, text="x = " + str(x) + ", y = " + str(y))
        b.grid(row=x, column=y, sticky="news", padx=5, pady=5)

for i in range(4):
    bottom.columnconfigure(i, weight=1)
    bottom.rowconfigure(i, weight=1)

root.mainloop()


