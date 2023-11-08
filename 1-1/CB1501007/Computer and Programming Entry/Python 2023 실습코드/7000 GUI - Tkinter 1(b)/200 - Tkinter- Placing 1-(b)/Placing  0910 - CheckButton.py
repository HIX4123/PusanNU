
#  CheckButton, RadioButton 출력위젯 Class를 이용해서 GUI 만들기
#  You can use the fill=X option to make all widgets as wide as the parent widget:

from tkinter import *   # Tkinter을 사용하기 위해 import

root = Tk()

frame = Frame(root)
frame.pack()
acount = 0

def Alchol():
    global acount
    acount += 1
    if acount %2 != 0 :
        print("알콜류 음료수를 선택하셨습니다.")
    else :
        print("알콜류 음료수를 취소하셨습니다.")


def Water():
    global acount
    acount += 1
    if acount %2 != 0 :
        print("생수를 선택하셨습니다.")
    else :
        print("생수를  취소하셨습니다.")

def Drinktype() :
    print("음료수 종류를 선택함", Rvalue)

iframe1 = Frame(frame, bd=3, relief= RAISED )
myBa = Checkbutton(iframe1, text='Alchol' , command=Alchol  ) # 버튼 만들고
myBa.pack(side=BOTTOM, padx=5)    # 만든 것을 반드시 메인화면에 채워야 한다.
myBb = Checkbutton(iframe1, text='Water' , command=Water  ) # 버튼 만들고
myBb.pack(side=LEFT, padx=5)    # 만든 것을 반드시 메인화면에 채워야 한다.
myBc = Checkbutton(iframe1, text='Juice' , command=Water  ) # 버튼 만들고
myBc.pack(side=LEFT, padx=5)    # 만든 것을 반드시 메인화면에 채워야 한다.


iframe1.pack()


root.mainloop()

