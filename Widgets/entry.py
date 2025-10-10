import tkinter as tk

root = tk.Tk()
root.title("Tkinter Entry")

def return_pressed(event):
    label.config(text=event.widget.get())

entry = tk.Entry(root)
entry.insert(0, "Digite seu texto!")
entry.bind("<Return>", return_pressed)
entry.pack(padx=5, pady=5, fill="x")

# A helper label to show the selected value
label = tk.Label(root, text="Entry demonstração!")
label.pack(padx=5, pady=5, fill="x")

root.mainloop()