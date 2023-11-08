#  Listbox widget 사용하기
#  참고자료 http://www.tutorialspoint.com/python/python_gui_programming.htm

from tkinter import *
import tkinter.messagebox
import tkinter

top = Tk()


def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))


Lb1 = Listbox(top, name='mylistbox' )
Lb1.insert(1, "1. Python")
Lb1.insert(2, "2. Perl")
Lb1.insert(3, "3. C")
Lb1.insert(4, "4. PHP")
Lb1.insert(5, "5. JSP")
Lb1.insert(6, "6. Ruby")
Lb1.pack()
Lb1.bind('<<ListboxSelect>>', onselect)



#Button( top, text="Var name", command=oneselect).pack()

top.mainloop()