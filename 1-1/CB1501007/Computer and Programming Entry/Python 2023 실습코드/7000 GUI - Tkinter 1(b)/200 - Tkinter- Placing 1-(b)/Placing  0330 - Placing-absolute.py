from tkinter import *   # tkinter을 사용하기 위해 import
from PIL import Image, ImageTk

#import ImageTk
#from PIL import Image   # 반드시 tkinter 다음에 선언에야 한다.

title= '절대좌표로 배치하기'

b1 = 0
b2 = 0

def mynote() :
    global b1
    b1 +=  1
    print("I clicked this button", b1 )
    if b1 >= 10 :
        exit()

def yournote() :
    global b2
    b2 += 1
    print( f'당신이 누른 횟수는 {b2}')

root = Tk();
root.title(title);

img = Image.open("image3.png")
print(img.size)
bardejov = ImageTk.PhotoImage( img )
mylabel = Label( image=bardejov)
mylabel.place(x=20, y=20)

# padx :  Additional padding left and right of the text.
# pady : Additional padding above and below the text.
# relief = { SUNKEN, RAISED, GROOVE, and RIDGE. }

# button size는 font의 배

B1 = Button(text = 'I am a button', bd=5, relief=RAISED,  command=mynote)
B1.config( height = 2, width = 15)
#B2 = Button(text = 'You are not a button', bd=5,  height = 1, width = 2, relief=RAISED, command=yournote)
B2 = Button(text = 'You are not a button', bd=5,  height = 1, bg="tomato", relief=RIDGE, command=yournote)
B1.place(x=10,y= 20)
B2.place(x=30,y= 80)


root.mainloop()



