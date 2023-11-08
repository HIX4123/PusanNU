#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------


from tkinter import *

count = 0

def keyPressed(event):
    # 키보드 문자하나 출력
    global count
    count += 1
    print( f'{count:3} > {event.char} {ord(event.char)}' )

root = Tk()

frame = Frame(root, width=100, height=100)
# Key 이벤트 바인딩
frame.bind('<Key>', keyPressed)
frame.place(x=0, y=0)

# 키보드 포커스를 갖게 한다. 어디에서나 키보드를 입력해도 된다.
# 모든 이벤트가 focus_set( )으로 정해진 frame으로 가게 된다.
frame.focus_set()

root.mainloop()
