
from tkinter import *

def get_text():
    myid = e1.get()
    print(" 입력한 단어=", myid,"\n 길이는 = ", len(myid))
    e1.delete(0,END)  # 화면에 입력된 것을 지움




master = Tk()
Label(master, text= "콜라 수").grid(row=100, column=100)


def quit2():
    master.destroy()

e1 = Entry(master)
e1.focus_set()            # 입력 커서를 이쪽으로  이것이 없으면 커서는 아무데나
e1.insert(10, "1병")
e1.grid(row=100, column=200)

Button(master, text= '중지', command= quit2).grid(row=200, column=100, sticky=W, pady=4)
Button(master, text= 'Show', command=get_text, bg='orange', \
       fg="blue").grid(row=200, column=200, sticky=W, pady=4)

mainloop( )
