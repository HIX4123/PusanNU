

from tkinter import *

def ok():
    print("GUI 창으로 입력한 값은 = ", entry.get())
    top.destroy()   # top을 없애면 전체가 사라진다.

root = Tk()             #  Tkinter process를 하나 만듭니다.
top  = Toplevel(root)    #  root를 최상위 프로세스로 만든다. 그이름은 top이다.
top2 = Toplevel(root)    #  root를 최상위 프로세스로 만든다. 그이름은 top이다.

label = Label(top, text=" 입력값(Value)")
label.pack()

label2 = Label(top2, text=" 출력값(Value)")
label3 = Label(top2, text=" 새로운 자식창 만들기")
label2.pack()
label3.pack()
#label.pack(side=LEFT)

# 입력공간을 만듬.
entry = Entry(top)
entry.pack(pady=15)  # 아래로 15 pixel을 띄어서 배치합니다.
button = Button(top, text="OK", command=ok, bg='black', fg='white')
button.pack()

top.title("Dialog Window")
#top.transient(root)
#root.wait_window(top)

root.mainloop()
