from tkinter import *

def get_text():
    myid = e1.get() # 입력창에 쓰여진 문자를 가지고 온다. get()
    print(" 입력한 단어=", myid,"\n 길이는 = ", len(myid))
    e1.delete(0,END)  # 화면에 입력된 것을 지움


master = Tk()
Label(master, text= "LOGIN: ").grid(row=100, column=100)


e1 = Entry(master)
e1.focus_set()            # 입력 커서를 이쪽으로  이것이 없으면 커서는 아무데나
e1.insert(10, "아무말 대잔치")
e1.grid(row=100, column=200)

Button(master, text= '중지', command=master.quit).\
                grid(row=200, column=100, sticky=W, pady=4)
Button(master, text= 'Show', command=get_text, bg='orange',  \
               fg="blue").grid(row=200, column=200, sticky=W, pady=4)

mainloop( )
