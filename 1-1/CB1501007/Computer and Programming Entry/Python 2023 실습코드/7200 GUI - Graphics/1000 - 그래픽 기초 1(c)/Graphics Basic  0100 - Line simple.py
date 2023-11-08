# 2023년 Line의 alpha 값 부분을 삭제. 지원하지 않음

from tkinter import *
root = Tk()     # 창을 하나 만듭니다.
root.title('간단하게 선 그려보기')

N=800
mypaper = Canvas(root, width= N, height= N, background="beige")
mypaper.create_line( 10,120 ,   N-30, N-290, width=6, fill='orange')
mypaper.create_line( 32, 780 ,  N-90,    90, width=8, fill='blue')
mypaper.create_line( 155,55 ,   159,56, width=3, fill='red')  # 점찍기
mypaper.create_text(150,100, font=("맑은 고딕",20), fill="blue", text="이것은 한글이다")

#mypaper.place(x=10, y=10) # pack() #grid( row=100, column=100)

mypaper.grid(row=0,column=0)   # 그려진 것을 꽉 차게 보여준다.
root.mainloop()

