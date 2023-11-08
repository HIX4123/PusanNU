

from tkinter import *

root =Tk()
root.geometry("300x400+30+30")  # 크기와 처음 놓는 위

root.title('엔트리 위젯(Entry widget)')
x= Label (text='화일 이름: ', bg="orange")
x.pack(  padx=10, pady=20)
# padx는 x축으로 양쪽으로 10 간격을 줌
# pady는 y축으로 아래 위로 20 간격을 줌

# 입력칸은 Entry로 결정합니다.
Entry(root, width=10, bg="yellow").pack( side=TOP, padx=0, pady=10) #밑에서 20 띄움

# 각종 버튼을 만들어 넣습니다.
Button(root, text='open', bg="orange" ).pack(side=  LEFT)
Button(root, text='edit' ).pack(side=  LEFT)
Button(root, text='exit' ).pack(side= RIGHT)
Button(root, text='close', bg="tomato", fg="white" ).pack(side= RIGHT)

root.mainloop()


