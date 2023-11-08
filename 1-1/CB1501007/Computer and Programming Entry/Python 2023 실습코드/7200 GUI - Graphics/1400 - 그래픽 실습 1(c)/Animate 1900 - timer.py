
#Tkinter -- Canvas의 사용법을 배웁니다. (Timer)
# after의 사용법
# after(time) : 단순히 time 만큼의 지연이 발생한다
# after(time, handler) : time시간 후 handler를 한번 호출 한다

from tkinter import *
import time
root = Tk()
root.title("[Problem Solving-UI] Canvas (Timer)")

canvas = Canvas(root, width=500, height=300, background="white")
canvas.pack()

count=0
cycle_period = 1000 # 새로 그리는 간격의 속도 단위는 milli second
flag = True

ball1 = canvas.create_oval(100, 100, 180, 180, fill='black')
ball2 = canvas.create_oval(300, 100, 380, 180, fill='black')
text = canvas.create_text(240, 100, text=str(count))
text2 = canvas.create_text(240, 250)

now = ball1 #현재 선택된 원

def handler():
    global now, text, count, timerId

    canvas.itemconfigure(ball1, fill='black')
    canvas.itemconfigure(ball2, fill='black')

    if now == ball1:
        canvas.itemconfigure(ball1, fill='green')
        now=ball2
    else :
        canvas.itemconfigure(ball2, fill='red')
        now=ball1
    print(' >')
    count+=1    #깜빡인 횟수를 하나 증가 시킴
    canvas.itemconfigure(text, text=str(count)) # 캔버스에 출력함

    if count == 10 : #10번 깜빡이면 타이머 종료
        canvas.after_cancel(timerId)
    else : #타이머를 새로 설정(reset)
        timerId = canvas.after(cycle_period, handler)

def handler2(): #handler2가 호출되면 flag를 False로 바꾼다
    global flag
    flag = False

def startA(): #timer와 독립적인 병행실행함수
    for i in range(1000):
        if i % 100 == 0:
            print(i)

def startX(): #timer에 종속적으로 실행될 함수
    global flag
    for i in range(10000):  #매번 flag를 체크하여 False가 될때까지 Loop를 돈다
        if flag == True :
            canvas.itemconfigure(text2, text=str(i))
            canvas.update()
        else : break
        canvas.after(100) #단순한 100ms의 지연 발생

timerId = canvas.after(cycle_period, handler) #handler()는 cycle_period초(1000milisecond)마다 호출 됨
#timerId = canvas.after(cycle_period, handler2) #handler2는 cycle_period초 후 중지

#병행 처리시작
startA()
#startX()

root.mainloop()
