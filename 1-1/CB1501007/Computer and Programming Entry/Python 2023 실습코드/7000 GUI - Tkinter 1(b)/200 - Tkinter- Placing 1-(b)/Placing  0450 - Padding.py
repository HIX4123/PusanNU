

from tkinter import *

root = Tk()

w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack()

w = Label(root, text="Green Grass", bg="green", fg="black")
#w.pack(pady=60)
w.pack()

w = Label(root, text="Blue Sky", bg="blue", fg="white")
#w.pack(fill=X,padx=30)  # 양쪽으로 10씩 띄움
w.pack()




mainloop()

