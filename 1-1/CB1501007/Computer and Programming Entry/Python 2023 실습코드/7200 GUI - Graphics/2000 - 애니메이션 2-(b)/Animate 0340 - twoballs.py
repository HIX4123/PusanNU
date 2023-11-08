
#Tkinter -- Canvas의 사용법을 배웁니다. (두개의 공의 rotations)

from tkinter import *
import time
root = Tk()
root.title("[Problem Solving-UI] Canvas (twoballs)")
cw = 350                                      # canvas width
ch = 200                                      # canvas height

GRAVITY = 1.5
chart_1 = Canvas(root, width=cw, height=ch, background="black")
chart_1.grid(row=0, column=0)

cycle_period = 80   # Time between new positions of the ball (milliseconds).
time_scaling = 0.2  # 위치의 변화를 계산할 때 다른 단계의 size를 governs.

# 매개 변수는 공의 면적과 위치를 결정
ball_1 = {'posn_x':25.0,     # x position of box containing the ball (bottom).
          'posn_y':180.0,    # x position of box containing the ball (left edge).
          'velocity_x':30.0,  # amount of x-movement each cycle of the 'for' loop.
          'velocity_y':100.0,    # amount of y-movement each cycle of the 'for' loop.
          'ball_width':20.0,   # size of ball - width (x-dimension).
          'ball_height':20.0,   # size of ball - height (y-dimension).
          'color':"dark orange",   # color of the ball
          'coef_restitution':0.90}   # proportion of elastic enrgy recovered each bounce

ball_2 = {'posn_x':cw - 25.0,     # x position of box containing the ball (bottom).
          'posn_y':300.0,    # x position of box containing the ball (left edge).
          'velocity_x':-50.0,  # amount of x-movement each cycle of the 'for' loop.
          'velocity_y':150.0,    # amount of y-movement each cycle of the 'for' loop.
          'ball_width':30.0,   # size of ball - width (x-dimension).
          'ball_height':30.0,   # size of ball - height (y-dimension).
          'color':"yellow3",   # color of the ball
          'coef_restitution':0.90}   # proportion of elastic enrgy recovered each bounce

def detectWallCollision(ball):
    # 벽과 충돌 감지
    if ball['posn_x'] > cw -  ball['ball_width']:           # 오른쪽 벽면과 충돌
        ball['velocity_x'] = -ball['velocity_x'] * ball['coef_restitution']  # 반대 방향으로 변경
        ball['posn_x'] = cw -  ball['ball_width']
    if  ball['posn_x'] <  1:                                # 왼쪽 벽면과 충돌
        ball['velocity_x'] = -ball['velocity_x'] *  ball['coef_restitution']
        ball['posn_x'] = 2                                 # anti-stick to the wall
    if  ball['posn_y'] <   ball['ball_height'] :            # 바닥과 충돌
        ball['velocity_y'] = -ball['velocity_y'] *  ball['coef_restitution']
        ball['posn_y'] = ball['ball_height']
    if  ball['posn_y'] > ch - ball['ball_height']:          # 천장과 충돌
        ball['velocity_y'] = - ball['velocity_y'] *  ball['coef_restitution']
        ball['posn_y'] = ch -  ball['ball_height']

def diffEquation(ball):
     # An approximate set of differential equations of motion for the balls
     ball['posn_x'] +=   ball['velocity_x'] * time_scaling
     ball['velocity_y'] =  ball['velocity_y'] + GRAVITY  # a crude equation incorporating gravity.
     ball['posn_y'] +=  ball['velocity_y'] * time_scaling
     chart_1.create_oval( ball['posn_x'],  ball['posn_y'],  ball['posn_x'] +  ball['ball_width'],\
                        ball ['posn_y'] +  ball['ball_height'], fill= ball['color'])
     detectWallCollision(ball)         # 공이 어떤 벽면과 충돌했는지?

for i in range(1,2000):       # 1000 position 이동 후 프로그램 종료

    diffEquation(ball_1)
    diffEquation(ball_2)

    chart_1.update()              # 캔버스 위에 새로 고쳐서 그린다.
    chart_1.after(cycle_period)   # 200ms 실행 일시 정지
    chart_1.delete(ALL)           # 모든 것을 지운다.

root.mainloop()
