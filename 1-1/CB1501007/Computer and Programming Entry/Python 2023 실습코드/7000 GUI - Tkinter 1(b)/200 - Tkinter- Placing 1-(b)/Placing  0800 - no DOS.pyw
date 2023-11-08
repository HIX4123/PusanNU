
# File: *.pyw 은 DOS 창의 띄우지 않고 결과만 보여준다. *.py 와 비교해보자.
from tkinter import *

root = Tk()     # Tk( )를 불러서 그 window의 이름을 root로 한다.

                # 레이블을 만듭니다. 그 위치는 root입니다.
                # text를 지정합니다. 한글도 가능합니다.

w = Label(root, text=u"내가 처음으로 만들어 본 창문 ㅎㅎㅎ!")

w.pack()        # w를 꽉.. 채워라. 이 명령이 실제 창을 만들어 보여준다.
#w.destroy( )   #이것을 사용하면 깡통 창문만 남게 된다.

root2 = Tk()
w2 = Label(root2, text=u"새로운 창문")
w2.pack()


root.mainloop()     # event loop을 수행한다.
                    # 계속 수행을 진행한다. 사용자의 반응을 기다리면사

