
from tkinter.ttk import Frame, Button, Style
from tkinter import Tk, BOTH
import tkinter.messagebox as box


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Message boxes")
        self.style = Style()
        self.style.theme_use("default")
        self.pack()

        error = Button(self, text="오류", command=self.onError)
        error.grid()
        warning = Button(self, text= "경고", command=self.onWarn)
        warning.grid(row=1, column=0)
        question = Button(self, text= "질문", command=self.onQuest)
        question.grid(row=0, column=1)
        inform = Button(self, text= "추가정보", command=self.onInfo)
        inform.grid(row=1, column=1)


    def onError(self):
        box.showerror("File Error", "화일을 열 수 없다니께.")

    def onWarn(self):
        box.showwarning("Warning", "함수호출 오류입니당. 다시 잘 찾아보셔")

    def onQuest(self):
        box.askquestion("Question", "Are you sure to quit?")

    def onInfo(self):
        box.showinfo("Information", "Download completed")


def main():
    root = Tk()
    ex = Example(root)
    root.geometry("300x150+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()