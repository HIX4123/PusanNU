
from tkinter import *

master = Tk()
warning = " 학교 성적 무시하면, 언젠가는 성적에게 무시당할거다. \n     조환규(1960- )"
callme =  " 지금하지 않은 일은 결국하지 못한다"

msg = Message(master, text = warning )
msg.config(bg='lightgreen', font=('times', 24, 'italic'))

msg2 = Message(master, text = callme )
msg2.config(bg='orange', font=('나눔명조', 24 ))

# 다 만든 메시지를 창에 우겨 넣
msg.pack( )
msg2.pack( )


mainloop( )
