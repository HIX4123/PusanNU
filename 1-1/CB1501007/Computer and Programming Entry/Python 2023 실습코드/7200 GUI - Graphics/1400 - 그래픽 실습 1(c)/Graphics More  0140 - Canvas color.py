
#Tkinter -- Canvas의 사용법을 배웁니다.

from tkinter import *
root = Tk()
tk_rgb = "#%02x%02x%02x" % (250, 250, 250) # 256 흰색  0 검정색


canvas = Canvas(root, bg=tk_rgb)
#canvas = Canvas(root, bg='dark turquoise') #캔버스 인스턴스(객체)생성 > Canvas도 하나의 위젯이다.
canvas.pack(fill=BOTH) #캔버스를 윈도우에 꽉차도록

#좌표계 예제
canvas.create_line(40,2, 200, 52, arrow='last', width=5)
canvas.create_line(10,2, 10, 200, arrow='first', width=5)
canvas.create_text(210, 10, text='x')
canvas.create_text(10, 210, text='y')

#직선을 이용한 예제
x1=0
y1=0
x2=100
y2=200
canvas.create_line(x1, y1, x2, y2, fill='red',width=7)
canvas.create_text(x2, y2, text='line #1')

x2=200
y2=100
canvas.create_line(x1, y1, x2, y2, fill='blue')
canvas.create_text(x2, y2, text='line #2')


#Window 가지고 놀기 : 윈도우 크기 조절

#실험 1. Window Size와 Canvas Size의 연동
def resize(event) :
    canvas.configure(width=event.width-4, height=event.height-4)

root.bind('<Configure>', resize )


#실험 2. Window Size 고정 : min과 max를 같은 크기로 설정하면 Size 고정
#root.minsize(width=420, height=240) #윈도우 최소크기 설정
#root.maxsize(width=420, height=240) #윈도우 최대크기 설정


#타이틀 설정
root.title("(Canvas Example)")
root.mainloop()