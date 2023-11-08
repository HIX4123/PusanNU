
from tkinter import *
from tkinter.filedialog import askopenfilename

class mywidgets:
	def __init__(self,root):
		frame=Frame(root)
		self.makeMenuBar(frame)
		self.txtfr(frame)
		frame.pack()
		return

	def txtfr(self,frame): #defines the text area
		textfr = Frame(frame)
		self.text = Text(textfr,height = 10,width = 50,background='white')
		scroll = Scrollbar(textfr)
		self.text.configure(yscrollcommand = scroll.set)
		self.text.pack(side = LEFT)
		scroll.pack(side = RIGHT,fill = Y)
		textfr.pack(side = TOP)
		return

	def makeMenuBar(self,frame): 	#defines menubar
		menubar = Frame(frame,relief = RAISED,borderwidth = 1)
		menubar.pack()
		mb_file = Menubutton(menubar,text = 'file')
		mb_file.pack(side = LEFT)
		mb_file.menu = Menu(mb_file)
		mb_file.menu.add_command(label = 'open',command = self.file_open)
		mb_edit = Menubutton(menubar,text = 'edit')
		mb_edit.pack(side = LEFT)
		mb_edit.menu = Menu(mb_edit)
		mb_edit.menu.add_command(label = 'copy')
		mb_help = Menubutton(menubar,text = 'help')
		mb_help.pack(padx = 25,side = RIGHT)
		mb_file['menu'] = mb_file.menu
 		mb_edit['menu'] = mb_edit.menu
		return

	def file_open(self): # 화일 open 할 때의 동작을 설정.
		root = Tk()
		filename =askopenfilename(filetypes=[("allfiles","*"),("pythonfiles","*.py")])
		print("선택한 화일의 이름은=", filename)



def main():
	root = Tk()
	k = mywidgets(root)
	root.title('interface')
	root.mainloop()

main()
