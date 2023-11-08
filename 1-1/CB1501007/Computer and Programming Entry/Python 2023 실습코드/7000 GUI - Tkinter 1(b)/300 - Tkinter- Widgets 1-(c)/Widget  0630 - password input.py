
from tkinter import *

def show_entry_fields():
    myid = e1.get()
    mypa = e2.get()
    if len(mypa) < 10 :
        print("10자리 이하의 password는 불가합니다.")
        return
    else :
        print("Login ID: %s  \nPassword : %s"  % ( myid, mypa ))
        e1.delete(0,END)
        e2.delete(0,END)

master = Tk()
Label(master, text="login ID").grid(row=0)
Label(master, text="password").grid(row=1)

e1 = Entry(master)
e2 = Entry(master, show="*")
#e1.insert(10,"A. Miller")
#e2.insert(10, u"김달수")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text= '중지', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text= 'Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
