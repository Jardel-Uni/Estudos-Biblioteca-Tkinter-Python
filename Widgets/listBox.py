import tkinter as tk

root = tk.Tk()
root.title("Listbox")

def selection_changed(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        label.config(text=f"{event.widget.get(index)} selecionado!")
        event.widget.get(index)

listbox = tk.Listbox(root)
for item in ["UM", "DOIS", "TRÊS"]:
    listbox.insert(tk.END, item)
listbox.bind("<<ListboxSelect>>", selection_changed)
listbox.pack(padx=5, pady=5, fill="both", expand=True)

label = tk.Label(root, text="UM selecionado!")
label.pack(padx=5, pady=5, fill="x")

root.mainloop()