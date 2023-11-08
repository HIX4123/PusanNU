from tkinter import *

root = Tk()
root.option_readfile('optionDB')
root.title('Message')

My = Message(root, text="Exactly.  It's my belief that these sheep are laborin' "
      "under the misapprehension that they're birds.  Observe their "
      "be'avior.  한글이 잘 됩니까 ?   Now witness their attmpts to "
      "fly from tree to tree.  Notice that they do not so much fly "
      "as...plummet.", bg='royalblue',
      fg='ivory', bd=5, relief=GROOVE)


My.pack(padx=10, pady=10)

root.mainloop()

