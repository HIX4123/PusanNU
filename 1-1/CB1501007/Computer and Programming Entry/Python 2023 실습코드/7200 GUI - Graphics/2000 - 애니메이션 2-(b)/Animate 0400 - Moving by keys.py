
#Tkinter -- Canvas의 사용법을 배웁니다. (Event Step2: Key Stroke)

from tkinter import *
root = Tk()
root.title( "Control Key  {w,s,a,d}  도움말 키:h")
canvas = Canvas(root, width=640, height=480, background="white")
canvas.pack()

class Sprite :
    delta=2  #변화량
    def __init__(self, item, c):  #생성자
        self.id = item
        self.color= c

    def moveTo(self, key):  #이동 함수, key : 눌려진 키
        global canvas
        if key == 'w':  #up
            canvas.move(self.id, 0, -self.delta)
        if key == 's':  #down
            canvas.move(self.id, 0, self.delta)
        if key == 'a':  #left
            canvas.move(self.id, -self.delta, 0)
        if key == 'd':  #right
            canvas.move(self.id, self.delta, 0)

def selectItem(event): #마우스 위치의 아이템을 선택하는 함수
    global selectedItem, BALL, ICON
    item = canvas.find_overlapping(event.x, event.y, event.x+1, event.y+1)  #마우스 위치에 있는 아이템 찾기
    #색 초기화
    canvas.itemconfigure(BALL.id, fill='black')
    canvas.itemconfigure(ICON.id, image=photo)

    if len(item)>0:
        if BALL.id == item[0] :
            canvas.itemconfigure(BALL.id, fill='red')
            selectedItem=BALL
            print("Selected item : BALL")
        elif ICON.id == item[0] :
            canvas.itemconfigure(ICON.id, image=photo2)
            selectedItem=ICON
            print("Selected item : ICON")
    else :
        selectedItem=-1
        print("No item")

def decodeKey(event):  #이벤트를 각 객체로 전달하는 함수
    if selectedItem != -1: #객체 이동
        selectedItem.moveTo(event.char)

def helpMenu(event):
    root2 = Tk()
    root2.title("Help")
    textList = ["[ Key List ]", "w - Up", "s - Down", "a - Left", "d - Right", "h - Help", "z - Quit"]
    for i in range(len(textList)):
        w = Label(root2, text=textList[i])
        w.pack()

def exitProgram(event):
    root.destroy()

#이벤트 바인딩
root.bind("<Button-1>", selectItem)  #한번 클릭, 해당 마우스 위치에 있는 아이템 선택
root.bind("<Key>", decodeKey) #키보드 입력, Object이동 이벤트 바인딩
root.bind("?", helpMenu) #키보드 입력, 도움말 창 생성
root.bind("z", exitProgram) #키보드 입력, 프로그램 종료

ballItem = canvas.create_oval(100, 100, 120, 120, fill='black')
BALL = Sprite(ballItem, 'black')

photo = PhotoImage(file='android.gif')
photo2 = PhotoImage(file='android2.gif')
iconItem = canvas.create_image(250, 100, image=photo)
ICON = Sprite(iconItem, 'black')

root.mainloop()
