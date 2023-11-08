from tkinter import *



root    = Tk()
root.geometry("600x300+500+500")
frame = Frame(root)
frame.pack()

bottomframe = Frame(root,bg="orangered" )
bottomframe.pack( side = BOTTOM )

redbutton =Button(frame, text="Red 빨강", fg="red")
redbutton.pack( side = RIGHT)


greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="파란색", fg="blue")
bluebutton.pack( side = LEFT )

xxx = Button(frame, text="교수님 짱짱먄", bg="tomato", fg="greenyellow")
xxx.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = TOP)

blackbutton = Button(bottomframe, text="아 술마시고 싶다", fg="black")
blackbutton.pack( side = TOP)

blackbutton = Button(bottomframe, text="Black2", fg="black")
blackbutton.pack( side = BOTTOM)

blackbutton = Button(bottomframe, text="아 술마시고 싶다2", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()