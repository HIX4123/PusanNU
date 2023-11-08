# !/usr/bin/python3
from tkinter import *
import tkinter

title="A Crazy Summer-Night"
root = Tk()
root.title(title)
root.geometry("400x300+300+100")
root.configure(bg="lightblue")
count=0

def mynote() :
    global count
    count += 1
    print (" +1 하나씩 올립니다.")
    Vlabel= Label(text="COUNT: "+ str(count)+"  ", bg="lightblue", font=("Arial",25))
    Vlabel.place(x=150, y=150)

def myset() :
    global count
    count = 0
    print (" 처음으로 되돌립니다.")
    Vlabel= Label(text="COUNT: "+ str(count)+"  ", bg="lightblue", font=("Arial",25))
    Vlabel.place(x=150, y=150)


def yournote() :
    print (" -1 하나씩 내립니다. ")
    global count
    count -= 1
    Vlabel= Label(text="COUNT: "+ str(count)+"  ", bg="lightblue", font=("Arial",25))
    Vlabel.place(x=150, y=150)


# relief = { RAISED, SUNKEN, RIDGE, GROOVE }

w = Button(text = 'Increase', bd=3, relief=RAISED ,  command=mynote, bg="orange")
R = Button(text = 'Reset',    bd=3, relief=RAISED ,  command=myset, bg="tomato")
Q = Button(text = 'Decrease', bd=3, relief=GROOVE, fg="blue", command=yournote)
w.place(x= 40,y=  20)
Q.place(x= 40,y=  70)
R.place(x= 40,y=  120)

Vlabel= Label(text="COUNT: "+ str( 0 )+"  ", bg="lightblue", font=("Arial",25))
Vlabel.place(x=150, y=150)
root.mainloop()
