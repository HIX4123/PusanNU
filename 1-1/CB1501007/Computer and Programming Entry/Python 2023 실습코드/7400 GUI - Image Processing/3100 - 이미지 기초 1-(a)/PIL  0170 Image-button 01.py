
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Vision and Vision")
root.geometry("500x480+300+300")


bard = Image.open("cocktail31.png")

print("image size=", bard.size)

bardejov = ImageTk.PhotoImage(bard)
#label1 = Button( root, text="sample",  bd=5)
label1 = Button( root,  image=bardejov, bd=5)
label1.place(x=120, y=120)


root.mainloop()