
# 화면을 늘이면 그대로 원 widget은 유지된다.

import tkinter
root = tkinter.Tk()
#root["bg"] = "khaki"
root.configure(background='green')

# label / entry pair
mylabela = tkinter.Label(root, text= "소속학과:", fg="blue", bg="khaki")
myentrya = tkinter.Entry(root)

# put in first row
mylabela.grid(row= 100, column= 100)
myentrya.grid(row= 100, column= 200)

# label / entry pair
mylabelb = tkinter.Label(root, text="College:", bg="orange")
myentryb = tkinter.Entry(root)

# put in first row
mylabelb.grid(row= 150, column= 100)
myentryb.grid(row= 170, column= 150)



root.mainloop()
