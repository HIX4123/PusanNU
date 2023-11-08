

from tkinter import *
from tkinter.colorchooser import askcolor

def callback():
    result = askcolor(color="#6A9662",
                      title = "Bernd's Colour Chooser")
    print(f'내가 선택한 칼라는={result}')
    print(result)

root = Tk()
root.title( "색상 선택하기 Widget")

Button(root, text='Choose Color', fg="darkgreen",
             command=callback).pack(side=LEFT, padx=10)
Button(text='Quit',
             command=root.quit,
             fg="red").pack(side=LEFT, padx=10)


mainloop()
