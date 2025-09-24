import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Demonstração")
root.minsize(200, 500)
root.maxsize(500, 500)
root.geometry("300x300+500+50")

widgets = [
    tk.Label,
    tk.Checkbutton,
    ttk.Combobox,
    tk.Entry,
    tk.Button,
    tk.Radiobutton,
    tk.Scale,
    tk.Spinbox,
]

for widget in widgets:
    try:
        widget = widget(root, text=widget.__name__)
    except tk.TclError:
        widget = widget(root)
    widget.pack(padx=5, pady=5, fill="x")

root.mainloop()