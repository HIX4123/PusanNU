
from tkinter import *
import tkinter


title="A Crazy Summer-Night"

root = Tk()
root.title(title);

def mynote() :
    print("I clicked this button")

def yournote() :
    print("당신은 학생 입니까 ? ")

# relief = { RAISED, SUNKEN, RIDGE, GROOVE }

w = Button(text = 'Moon', bd=5, relief=GROOVE,  command=mynote, bg="orange")
Q = Button(text = 'Earth', bd=5, font=("맑은 고딕 Bold",12), relief=RAISED, fg="blue", command=yournote)
Q.configure(height=1, width=10)  # size를 조정함.
w.place(x=10,y= 20)
Q.place(x=30,y= 80)


root.mainloop()
