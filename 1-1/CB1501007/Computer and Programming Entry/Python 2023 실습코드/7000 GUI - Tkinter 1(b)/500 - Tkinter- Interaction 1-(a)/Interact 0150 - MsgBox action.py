
from tkinter import *
import tkinter.messagebox


def callback():
    if tkinter.messagebox.askokcancel("Quit", "정말로 끝짱을 볼 생각입니까?"):
        root.destroy()          # 시작 task를 끝내고 전체 수행을 종

root = Tk()
root.protocol("WM_DELETE_WINDOW", callback)   # x로 마크된 기호를 누르면 발생
root.mainloop()