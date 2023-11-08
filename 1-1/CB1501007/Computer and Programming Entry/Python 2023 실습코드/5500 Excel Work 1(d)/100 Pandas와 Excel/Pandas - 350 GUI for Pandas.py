#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df

    file_path = filedialog.askopenfilename()
    df = pd.read_excel ( file_path )
    print("\n > ", file_path.split('/')[-1], " <\n")
    print(df)



browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, \
                 bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)



root.mainloop()
