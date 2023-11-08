from tkinter import *

class mywidgets:
	def __init__(self,root):
		frame=Frame(root)
		frame.pack()
		self.txtfr(frame)
		return

	def txtfr(self,frame):

		textfr=Frame(frame) # ??? frame? ????.
		self.text=Text(textfr,height=10,width=50,background='khaki')

		scroll=Scrollbar(textfr) # put a scroll bar in the frame
		self.text.configure(yscrollcommand=scroll.set)

		#pack everything
		self.text.pack(side=LEFT)
		scroll.pack(side=RIGHT,fill=Y)
		textfr.pack(side=TOP)
		return

def main():
	root = Tk()
	s=mywidgets(root)
	root.title('textarea')
	root.mainloop()

main()

