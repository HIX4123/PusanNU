from tkinter import *
master = Tk()

def var_states():
   print(("male: %d,\nfemale: %d" % (var1.get(), var2.get())))
   print(("Puppy: %d " % (var3.get()) ))

Label(master, text="Your sex:").grid(row=0, sticky=W)

def outout():
    exit()


var1 = IntVar()
Checkbutton(master, text="남성(male)", fg="red", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="여성(female)", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="강아지(puppy)", fg="purple",  variable=var3).grid(row=3, sticky=W)

Button(master, text='Quit', command=master.quit).grid(row=6, sticky=W, pady=4)
Button(master, text='Show', command=var_states ).grid(row=7, sticky=W, pady=4)

mainloop()
