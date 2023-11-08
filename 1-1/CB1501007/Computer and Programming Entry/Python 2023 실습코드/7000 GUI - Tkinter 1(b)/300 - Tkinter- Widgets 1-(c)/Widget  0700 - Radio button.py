
from tkinter import *

root = Tk()

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():
    print(v.get())

Label(root,
      text= "사용할 언어를 선택하세요.",
      justify = LEFT,
      padx = 20).pack()

for txt, val in languages:
    Radiobutton(root,
                text=txt,
                padx = 20,
                variable=v,
                command=ShowChoice,
                value=val).pack(anchor=W)

# 아래 부분을 지워 봅시다.
for txt, val in languages:
    Radiobutton(root,
                text=txt,
                indicatoron = 0,
                width = 20,
                padx = 20,  bg="green",
                variable=v,
                command=ShowChoice,
                value=val).pack(anchor=W)


mainloop()
