import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import psycopg2 as psc

class App(tk.Tk): #App eh uma subclasse de Tk
    def __init__(self):
        super().__init__()
        #construtor de app que chama o construtor de Tk
        self.title("Tela1")
        self.geometry("1200x800")

        self.label = ttk.Label(self, text = "Primeira Label")
        self.label.pack()

        self.button = ttk.Button(self, text = "Click!", command = self.button_clicked)


if __name__ == "__main__":
    app = App()
    app.mainloop()
