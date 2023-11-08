
#Tkinter -- Canvas의 사용법을 배웁니다. (Color Wheel)

from tkinter import *
root = Tk()
root.title("[Problem Solving-UI] Canvas (Color Wheel)")

cw = 300                                      # canvas width
ch = 300                                      # canvas height
canvas_1 = Canvas(root, width=cw, height=ch, background="black")
canvas_1.grid(row=0, column=1)
cycle_period = 200

redFl = 255.0
greenFl = 0
blueFl = 0
kula = "#000000"

arcStart = 89
arcEnd = 90

xCentr = 150
yCentr = 160
radius = 130
circ = xCentr - radius, yCentr + radius, xCentr + radius, yCentr - radius

# angular position markers, degrees
A_ANG = 0
B_ANG = 60
C_ANG = 120
D_ANG = 180
E_ANG = 240
F_ANG = 300
#G_ANG = 1
G_ANG = 359
intervals = 60 # degrees

# 마커의 각 위치별 색상 비율
# index        0    1    2   3    4    5    6   7
redShift   = 100, 100,   0,   0,   0, 100, 100    # 빨강
greenShift =  0,  100, 100, 100,   0,   0,   0    # 초록
blueShift  =  0,    0,   0, 100, 100, 100,   0    # 파랑

# Rate of change of color per degree, rgb integer counts per degree.
red_rate = [0,1,2,3,4,5,6,7]
green_rate = [0,1,2,3,4,5,6,7]
blue_rate = [0,1,2,3,4,5,6,7]

# Calibrate counts-per-degree in each interval, place in xrate list
for i in range(0,6):
    red_rate[i] = 256.0 * (redShift[i+1]   - redShift[i])/(100 * intervals)
    green_rate[i] = 256.0 * (greenShift[i+1] - greenShift[i])/(100 * intervals)
    blue_rate[i] = 256.0 * (blueShift[i+1]  - blueShift[i])/(100 * intervals)

def rgb2hex(redFl, greenFl, blueFl):
    # 16진수로 변환
    red = int(redFl)
    green = int(greenFl)
    blue = int(blueFl)
    rgb = red, green, blue
    return '#%02x%02x%02x' % rgb

for i in range (0, 359):
    canvas_1.create_arc(circ, start=arcStart, extent=arcStart - arcEnd,\
                        fill= kula, outline= kula)
    arcStart = arcEnd
    arcEnd -=1

    # 색 요소 변환 (60 degree sectors)
    if  i>A_ANG and i<B_ANG:
        redFl   +=  red_rate[0]
        greenFl +=  green_rate[0]
        blueFl  += blue_rate[0]
        kula = rgb2hex(redFl, greenFl, blueFl)

    if  i>B_ANG and i<C_ANG:
        redFl   +=  red_rate[1]
        greenFl +=  green_rate[1]
        blueFl  +=  blue_rate[1]
        kula = rgb2hex(redFl, greenFl, blueFl)

    if  i>C_ANG and i<D_ANG:
        redFl   +=  red_rate[2]
        greenFl +=  green_rate[2]
        blueFl  +=  blue_rate[2]
        kula = rgb2hex(redFl, greenFl, blueFl)

    if  i>D_ANG and i<E_ANG:
        redFl   +=  red_rate[3]
        greenFl +=  green_rate[3]
        blueFl  +=  blue_rate[3]
        kula = rgb2hex(redFl, greenFl, blueFl)

    if  i>E_ANG and i<F_ANG:
        redFl   +=  red_rate[4]
        greenFl +=  green_rate[4]
        blueFl  +=  blue_rate[4]
        kula = rgb2hex(redFl, greenFl, blueFl)

    if  i>F_ANG and i<G_ANG:
        redFl   +=  red_rate[5]
        greenFl +=  green_rate[5]
        blueFl  +=  blue_rate[5]
        kula = rgb2hex(redFl, greenFl, blueFl)

    #kula = rgb2hex(redFl, greenFl, blueFl)
    canvas_1.create_text(100, 20,  text=kula, fill='white', width=200,\
                font='SansSerif 12 ', tag= 'degreesAround', anchor= SW)
    canvas_1.update()                   # 캔버스 위에 새로 고쳐서 그린다.
    canvas_1.after(cycle_period)        # 200ms 실행 일시 정지
    canvas_1.delete('degreesAround')    # 변화된 text 삭제

root.mainloop()