

from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )


redbutton   = Button(frame, relief=RAISED, bg='white', text="다람쥐", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, relief=RAISED,text="호랑이", bg='black', fg="white")
greenbutton.pack( side = RIGHT )

bluebutton  = Button(frame, relief=RAISED,text="너구리", bg='lightblue', fg="blue")
bluebutton.pack( side = BOTTOM )

blackbutton = Button(bottomframe,relief=SUNKEN, text="돌고래", bg='yellow', fg="black")
blackbutton.pack( side = LEFT )

bluebutton  = Button(frame, relief=RAISED,text="딱다구리", bg="pink")
bluebutton.pack( side = TOP )

bluebutton  = Button(frame, relief=RAISED,text="도다리", bg="khaki")
bluebutton.pack( side = RIGHT )

bluebutton  = Button(frame, relief=RAISED,text="두꺼비", bg="salmon")
bluebutton.pack( side = TOP )


root.mainloop()