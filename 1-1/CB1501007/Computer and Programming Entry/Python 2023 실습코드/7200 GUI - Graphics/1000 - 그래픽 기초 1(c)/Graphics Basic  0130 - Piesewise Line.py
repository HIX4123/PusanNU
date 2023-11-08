
from tkinter import *
root = Tk()     # 창을 하나 만듭니다.
root.title(' 꺾은 선 그려보기')

N=800

xylist= [ 10, 10, 488, 153, 70, 450, 650, 74, 414, 653, 349, 100, 39, 43, 10, 10 ]

mypaper = Canvas(root, width= N, height= N, background="light green")
mypaper.create_line( xylist, width=3, fill='red' )  # 점찍기
# mypaper.create_text(150,100, font=("맑은 고딕",20), fill="blue", text="이것은 한글이다")

mypaper.pack()   # 그려진 것을 꽉 차게 보여준다.


root.mainloop()


