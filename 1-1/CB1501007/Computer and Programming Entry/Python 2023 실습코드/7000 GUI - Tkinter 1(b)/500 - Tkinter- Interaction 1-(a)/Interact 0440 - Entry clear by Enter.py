
import tkinter as tk

def on_enter(event):
    widget = event.widget
    print("\n Input=>>> ", (widget.get()))
    widget.delete(0, "end")



root = tk.Tk()
entry = tk.Entry(show="*")
entry.pack(padx=5, pady=5)
entry.focus()
entry.bind('<Return>', on_enter)
root.mainloop()

