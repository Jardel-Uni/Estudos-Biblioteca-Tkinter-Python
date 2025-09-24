import tkinter as tk
root = tk.Tk()

root.title("Exemplo")
root.configure(background="White")
root.minsize(200, 500)
root.maxsize(500, 500)
root.geometry("300x300+500+50") #largura x altura - posição na tela +

tk.Label(root, text="Nada funcionará a menos que você faça.").pack()
tk.Label(root, text="- Maya Angelou").pack()

image = tk.PhotoImage(file="Criando-Janela\pikachu.png")   #pode ser usado o caminho absoluto
tk.Label(root, image=image).pack()

root.mainloop()

