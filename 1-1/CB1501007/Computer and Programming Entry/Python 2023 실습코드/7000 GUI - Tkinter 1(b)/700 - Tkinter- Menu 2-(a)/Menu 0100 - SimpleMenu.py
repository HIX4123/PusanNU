

from tkinter import Tk, Frame, Menu


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title( "Simple Menu Making")
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu01 = Menu(menubar)
        fileMenu01.add_command(label="Exit",  command = self.onExit)
        fileMenu01.add_command(label="Quit",  command = self.onQuit)
        menubar.add_cascade(label="File",   menu=fileMenu01)

        fileMenu02 = Menu(menubar)
        fileMenu02.add_command(label="MyWork",  command = self.onMyWork)
        menubar.add_cascade(label="Photo",  menu=fileMenu02)
        menubar.add_cascade(label="Sound",  menu=fileMenu02)



    def onExit(self):
        print("exit 합니다")
        self.quit()


    def onQuit(self):
        print("Quit( )를 실행하고 종료합니다.")
        self.quit()

    def onMyWork(self):
        print("MyWork 메뉴를 선택했습니다.")


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()

