

from tkinter import *

root =Tk()
root.geometry("600x400+30+30")  # 크기와 처음 놓는 위
root.configure(bg="tan")
mystyle= ('나눔고딕', 35, 'bold')

x01 = 30
x02 = 250
y01 = 50
y02 = 150

def get_text():
    myid = mydone.get()
    print(" 입력한 단어=", myid,"\n 길이는 = ", len(myid))
    mydone.delete(0,END)  # 화면에 입력된 것을 지움

def shopdone( ):
    print("구매완료했습니다" )
    # fp = open("KKD_order.txt", "w")


root.title('엔트리 위젯(Entry widget)')
Label (text='Zoh 아저씨의 티켓숍: ', bg="tan", font=mystyle ).place( x=x01, y=y01)
Label (text='구매자 이름: ', bg="orange", height=2, width=10 ).place(  x=x01, y=y02)
# padx는 x축으로 양쪽으로 10 간격을 줌
# pady는 y축으로 아래 위로 20 간격을 줌

# 입력칸은 Entry로 결정합니다.
mydone = Entry(root, width=12,  bg="yellow" )
mydone.place( x=x02, y=y02 ) #밑에서 20 띄움

# 각종 버튼을 만들어 넣습니다.
Button(root, text='구매완료', font=('나눔명조', 20, 'bold'),\
        command=get_text, relief=RIDGE, bd=5 ).place(x=x01, y=300)


root.mainloop()


