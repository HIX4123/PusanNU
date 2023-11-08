
from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.parent.title( "라인(Lines) 그려보기")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 25, width=3)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2), width=5)
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 185, width=3, fill="red" )
        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example(root)
    root.geometry("800x850+300+300")
    root.mainloop()



if __name__ == '__main__':
    main()