from tkinter import *
from tkinter.filedialog import askopenfilename

def main():

 	root=Tk()
	filename = askopenfilename(filetypes=[("allfiles","*"),("pythonfiles","*.py")])

main()
