

# 화면을 늘이면 그대로 원 widget은 유지된다.

import tkinter
root = tkinter.Tk()

mystyle= ('나눔고딕', 18, 'bold')

# label / entry pair
mylabela = tkinter.Label(root, text="성씨:", fg="red", font=mystyle )
myentrya = tkinter.Entry(root)

# put in first row
mylabela.grid(row= 100, column= 100)
myentrya.grid(row= 100, column= 200)

# label / entry pair
rtext= "이름"

mylabelb = tkinter.Label(root, text=rtext,  font=mystyle)
myentryb = tkinter.Entry(root)

# put in first row
mylabelb.grid(row= 200, column= 100)
myentryb.grid(row= 200, column= 200)

# label / entry pair
l3 = tkinter.Label(root, text="몇살인교?:", font=mystyle)
e3 = tkinter.Entry(root)

# put in first row
l3.grid(row= 300, column= 100)
e3.grid(row= 300, column= 200)

root.mainloop()
