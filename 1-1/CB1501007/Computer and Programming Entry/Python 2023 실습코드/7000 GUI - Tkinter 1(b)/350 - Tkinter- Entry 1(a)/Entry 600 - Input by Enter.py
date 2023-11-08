
import tkinter as tk

def on_enter(event):
    widget = event.widget
    print("\n Input=>>> ", (widget.get()))
    widget.delete(0, "end")



root = tk.Tk()
root.title("매스워드용 Entry")
entry = tk.Entry(show="*")
entry.place(x=20, y=50)
entry.focus()  # 커서를 여기 entry 넣어서 대기...
entry.bind('<Return>', on_enter)
root.mainloop()

