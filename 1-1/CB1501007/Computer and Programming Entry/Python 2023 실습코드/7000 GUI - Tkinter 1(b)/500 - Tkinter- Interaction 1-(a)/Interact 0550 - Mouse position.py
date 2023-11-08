
from tkinter import *

def motion(event):
  print(("Mouse position: (%s %s)" % (event.x, event.y)))
  return

master = Tk()
master.title("MAYA!")
whatever_you_do = "착하게 살자 \n 조용히 살자 "
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))

msg.bind('<Motion>',motion)

msg.pack()
mainloop()

