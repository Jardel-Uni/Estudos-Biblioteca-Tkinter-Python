import tkinter as tk

root = tk.Tk()
root.title("Tkinter Label")
root.geometry("600x600")

label = tk.Label(root, text="Hello!", font=("Helvetica", 30))
#label = tk.Label(root, anchor="c")
#label.config(text="Oi") #alterar
photo = tk.PhotoImage(file="Widgets\png-transparent-cute-cat-smiling-cat-thumbnail.png")
label2 = tk.Label(root, image=photo)



label.pack(expand=True)
label2.pack(expand=True)

root.mainloop()
