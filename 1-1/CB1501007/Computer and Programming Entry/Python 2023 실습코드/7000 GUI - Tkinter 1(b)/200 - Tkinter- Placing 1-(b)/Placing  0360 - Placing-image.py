from tkinter import *   # tkinter을 사용하기 위해 import
from PIL import Image, ImageTk  # 반드시 tkinter 다음에 선언에야 한다.


title= '절대좌표로 배치하기'

def mynote() :
    print("I clicked this button")

def yournote() :
    print("당신은 학생 입니까 ? ")

root = Tk();
root.title(title);

img = Image.open("image3.png")
print(img.size)
bardejov = ImageTk.PhotoImage( img )
mylabel = Label( image=bardejov)
#mylabel.image = bardejov
mylabel.place(x=60, y=20)

# padx :  Additional padding left and right of the text.
# pady : Additional padding above and below the text.
# relief = { SUNKEN, RAISED, GROOVE, and RIDGE. }

w = Button(text = 'I am a button', bd=5, relief=SUNKEN,  command=mynote)
Q = Button(text = 'You are not a button', bd=5, relief=RAISED, command=yournote)
w.place(x=10,y= 20)
Q.place(x=30,y= 80)


root.mainloop()



