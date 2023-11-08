
#Tkinter -- Canvas의 사용법을 배웁니다. (Event Step2: Key binding)

from tkinter import *
root = Tk()
root.title( "키보드 처리하기 (종료=z")
canvas = Canvas(root, width=500, height=400, background="khaki")
canvas.pack()

def decodeKey(event):  #눌려진 키를 출력하는 함수
    key = event.char
    print('You pressed'+'[ '+key+' ]')

def exitProgram(event):
    root.destroy()

#이벤트 바인딩
root.bind("<Key>", decodeKey)   #키보드 입력, 눌려진 버튼 출력
root.bind("z", exitProgram)     #키보드 입력, 프로그램 종료

root.mainloop()
