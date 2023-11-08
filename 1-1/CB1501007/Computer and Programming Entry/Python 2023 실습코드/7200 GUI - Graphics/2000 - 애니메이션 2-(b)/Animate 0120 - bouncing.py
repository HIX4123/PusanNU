
#Tkinter -- Canvas의 사용법을 배웁니다. (튀는 공에 대한 simulation)
#  과제 - 공이 정확하게 경계면에서 반사하게 만들기
#          'w'키를 누르면 진행방향을 반대로 하기 (global 선언)
#          공의 크기를 마음대로 바꾸기

from tkinter import *
import time

root = Tk()
root.title("튀는 공을 잡아라")
cw = 300                                      # canvas width
ch = 200                                      # canvas height
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=30, column=50)

cycle_period = 20   # 새로 그리는 간격의 속도 단위는 milli second

# 매개 변수는 공의 면적과 위치를 결정
posn_x  =     1    # x position of box containing the ball (bottom).
posn_y  =     1    # x position of box containing the ball (left edge).
shift_x  =    1    # amount of x-movement each cycle of the 'for' loop.
shift_y  =    1    # amount of y-movement each cycle of the 'for' loop.

# 공에 대한 정의(definition)
ball_width =  25   # size of ball - width (x-dimension).
ball_height = 25   # size of ball - height (y-dimension).
color = "darkgreen"   # color of the ball
out = 0

def detectWallCollision(): # 충돌 감지 및 방향 전환
    global posn_x, posn_y, shift_x, shift_y, cw, cy
    if posn_x > cw :           # 오른쪽 벽면과 충돌
        shift_x = -shift_x         # 반대 방향으로 변경
    if posn_x <  0 :           # 왼쪽 벽면과 충돌
        shift_x = -shift_x
    if posn_y > ch  :          # 바닥과 충돌
        shift_y = -shift_y
    if posn_y <  0 :           # 천장과 충돌
        shift_y = -shift_y

def decodeKey(event):  #눌려진 키를 출력하는 함수
    global out, root
    key = event.char
    print(key+' pressed')
    if key == 'z' :
        #sys.exit()
        root.destroy()




def exitProgram(event):
    global outw
    root.stop()

#이벤트 바인딩
root.bind("<Key>", decodeKey) #키보드 입력, 눌려진 버튼 출력



N = 1000
for i in range(1, N ):       # N번 반복한다.
    posn_x +=  shift_x
    posn_y +=  shift_y

    chart_1.create_oval(posn_x, posn_y, posn_x + ball_width,\
                        posn_y + ball_height, fill=color)
    detectWallCollision()         # 공이 어떤 벽면과 충돌했는지?
    chart_1.update()              # 캔버스 위에 새로 고쳐서 그린다.
    chart_1.after(cycle_period)   # 200ms 실행 일시 정지
    chart_1.delete(ALL)           # 모든 것을 지운다.
    if i % 100 == 0 : print(" >", out)
    if out == 1 : break

print("모든 동작이 종료되었습니다")
root.mainloop()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.>>>>>>
