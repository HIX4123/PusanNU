import tkinter

root1 =  tkinter.Tk()  # 창만들기, task를 하나 뿅...
root2 =  tkinter.Tk()

root1.geometry("600x300+500+500")  # 크기와 window가 처음 놓일 위치
root1.title( "root 1 - 오 재미있네요 ")
root2.title( "root 2 - 뭐여 이건? ")


#  만들기
mf = tkinter.Frame(root1, bg="tomato") #background

# 변수, 판때기, 버튼, Entry......

# 놓기, 위치시키기
mf.place(height=150, width=300, x=100, y=50)

mg = tkinter.Frame(root1, bg="green")
mg.place(height=60, width=60, x=80, y=120)



mr = tkinter.Frame(root2, bg="red")
mr.place(height=60, width=60, x=100, y=100)

root1.mainloop()
#root2.mainloop()
print("끝이 납습니다. ")
