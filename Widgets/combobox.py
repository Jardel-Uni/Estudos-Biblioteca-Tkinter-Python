import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox")
root.geometry("500x200")

def selection_change(event):
    label.config(text=f"{event.widget.get()} selecionado!")

#combobox = ttk.Combobox(root, values=["UM", "DOIS", "TRÊS"])
combobox = ttk.Combobox(root, values=["UM", "DOIS", "TRÊS"], state="readonly")
combobox.set("UM")
combobox.bind("<<ComboboxSelected>>", selection_change)
combobox.pack(padx=5, pady=5, fill="x")

label = tk.Label(root, text="Um Selecionado!")
label.pack(padx=5, pady=5, fill="x")

root.mainloop()
