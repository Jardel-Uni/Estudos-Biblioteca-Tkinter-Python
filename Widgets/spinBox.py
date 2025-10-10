import tkinter as tk

root = tk.Tk()
root.title("Tkinter Spinbox")
root.geometry("200x80")

spinbox_var = tk.StringVar(value="0")
spinbox = tk.Spinbox(
    root,
    from_=-10,
    to=10,
    textvariable=spinbox_var,
)
spinbox.pack(padx=5, pady=5, fill="x")

label = tk.Label(root, textvariable=spinbox_var)
label.pack(padx=5, pady=5, fill="x")

root.mainloop()