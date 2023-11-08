
from tkinter import *


root = Tk()         # create a Tk root widget
root["bg"]="orange"

msg1 = Label(root, text= "Hello ! 부산대학교 Tkinter! \n 열심히 해 봅시다.")
msg2 = Label(root, text= "준비가 되었습니까 ? ",  bg='khaki', font = ( "맑은 고딕",30), fg="blue" )

msg1.pack()            # The pack : Tk to fit the size of the window to the given text.
msg2.pack()

root.mainloop()
