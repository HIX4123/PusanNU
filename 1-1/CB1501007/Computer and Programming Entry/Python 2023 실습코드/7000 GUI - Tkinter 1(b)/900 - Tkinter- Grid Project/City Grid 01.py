

from tkinter import *

root =Tk()
root.geometry("800x600+30+30")  # 크기와 처음 놓는 위

root.title('Cop and Robber Experiment')
Label (text='화일 이름: ', bg="orange").pack(  padx=10, pady=20)
# padx는 x축으로 양쪽으로 10 간격을 줌
# pady는 y축으로 아래 위로 20 간격을 줌

# 입력칸은 Entry로 결정합니다.
Entry(root, width=15, bg="yellow").pack( side=TOP, padx=0, pady=10) #밑에서 20 띄움

# 각종 버튼을 만들어 넣습니다.
Button(root, text='Cop Move' ).pack(side=  TOP)
Button(root, text='Robber Move' ).pack(side=  TOP)
Button(root, text='Random Set' ).pack(side= TOP)
Button(root, text='Set Strategy').pack(side= TOP)

root.mainloop()


