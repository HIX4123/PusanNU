#-*- coding: cp949 -*-

# ȭ���� ���̸� �״�� �� widget�� �����ȴ�.

import Tkinter
root = Tkinter.Tk()

# label / entry pair
mylabela = Tkinter.Label(root, text=u"First Name �� ��:", fg="red")
myentrya = Tkinter.Entry(root)

# put in first row
mylabela.grid(row= 100, column= 100)
myentrya.grid(row= 100, column= 200)

# label / entry pair
mtext="�̸�"
rtext = unicode( mtext) #, 'utf-8')
mylabelb = Tkinter.Label(root, text=rtext)
myentryb = Tkinter.Entry(root)

# put in first row
mylabelb.grid(row= 200, column= 100)
myentryb.grid(row= 200, column= 200)

# label / entry pair
l3 = Tkinter.Label(root, text=u"����α�?:")
e3 = Tkinter.Entry(root)

# put in first row
l3.grid(row= 300, column= 100)
e3.grid(row= 300, column= 200)

root.mainloop()
