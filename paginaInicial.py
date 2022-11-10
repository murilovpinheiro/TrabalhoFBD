import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.title("Tela Inicial")
menubar = tk.Menu(root)
root.config(menu = menubar)

menu = tk.Menu(menubar, tearoff = False)

menu.add_command(label = 'Exit',
                 command = root.destroy)

menu.add_command(label = 'Adicionar',
                 command = root.destroy)

menubar.add_cascade(
    label = 'File',
    menu = menu,
)
frames = {}
frame = tk.Frame(parent = root)
frame.grid(row=0, column=0, sticky="nsew")
frames[0] = frame

root.mainloop()