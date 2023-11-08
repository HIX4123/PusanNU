


from tkinter import *

root = Tk()

root.title("Summer")
root.geometry("200x100+30+30")

w = Label(root, text="Red Sun", bg="red", fg="white").pack()
w = Label(root, text="Green Grass", bg="green", fg="black").pack()
w = Label(root, text="Blue Sky", bg="blue", fg="white").pack()

root2 = Tk()
root2.geometry("200x100+30+30")
root.title("Winter")
w = Label(root2, text="빨간 태양", bg="red", fg="white").pack(fill=X)
w = Label(root2, text="파란색 풀밭", bg="green", fg="black").pack(fill=X)
w = Label(root2, text="파란색 하늘 하늘", bg="blue", fg="white").pack(fill=X)

mainloop()
