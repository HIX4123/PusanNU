#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-05-28
#-------------------------------------------------------------------------------

import tkinter as tk



class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.root.geometry('300x200')
       button = tk.Button(self.root,
                          text = 'Click and Quit',
                          command=self.quit)
       button.pack()
       self.root.mainloop()

   def quit(self):
        print("끝납니다.")
        self.root.destroy()

app = Test()
