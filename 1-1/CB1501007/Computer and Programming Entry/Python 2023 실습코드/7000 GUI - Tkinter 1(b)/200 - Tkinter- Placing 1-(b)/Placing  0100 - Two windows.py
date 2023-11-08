
# File: *.pyw 은 DOS 창의 띄우지 않고 결과만 보여준다. *.py 와 비교해보자.
from tkinter import *

root = Tk()     # Tk( )를 불러서 그 window의 이름을 root로 한다. root 위
                # 레이블을 만듭니다. 그 위치는 root입니다.
                # text를 지정합니다. 한글도 가능합니다.
w = Label(root, text="root 중국집 창문", bg="orange")
w.pack()        #  실제 창을 만들어 보여준다.
#w.destroy( )   # 이것을 사용하면 깡통 창문만 남게 된다.

root2 = Tk()
w2 = Label(root2, text="root2 이탈리안 피잣집 \n Italian Pizza", bg="azure")
w2.pack()       # 이 창을 닫아도 root는 그대로 살아있다. main이 아니기 때문.


root.mainloop()     # event loop을 수행한다.
                    # 계속 수행을 진행한다. 사용자의 반응을 기다리면사

