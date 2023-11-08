# https://blog.resellerclub.com/the-6-best-python-gui-frameworks-for-developers/
# 잘 알려진 대표적인 Python GUI


import tkinter

root1 = tkinter.Tk()  # Tk( ) 하나 당 하나의 task을 만들고 #창을 생성
root1.title("root1 : My Window")


root2 = tkinter.Tk()
root2.title("root2 : 내 창문이란 말이다. 내 창문")

root3 = tkinter.Tk()
root3.title("root3 : 오메 이것이 뭐시다냐?")



root1.mainloop() # 돌려라, 돌려, 계속적으로
root2.mainloop()  # 사용자의 GUI환경에서의 입력을 기다림.

print("끄읃......")

# event-driven 프로그램