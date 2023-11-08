
import tkinter

root = tkinter.Tk()
root.config(width=600, height=400, background="orange")

b1 = tkinter.Label(root,  text="rela (0.5, 0.5)", fg="red", bg="black")
b2 = tkinter.Button(root, text="(220,220)")
b3 = tkinter.Button(root, text="rela (0.2, 0.8)")

# place b1's top left corner at the middle
b1.place(relx=.5, rely=.5)

# place b2's top left corner at the top left
b2.place(x=220, y=220)

# somewhere near the bottom left
b3.place(relx=.2, rely=.8)


root.mainloop()


