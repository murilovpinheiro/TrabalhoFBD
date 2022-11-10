import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from telaSaida import *

class App(tk.Tk): #App eh uma subclasse de Tk
    def __init__(self):
        super().__init__()
        #construtor de app que chama o construtor de Tk
        self.title("Tela1")
        self.geometry("1200x800")

        self.label = ttk.Label(self, text = "Primeira Label")
        self.label.pack()

        self.button = ttk.Button(self, text = "Click!", command = self.button_clicked)
        self.button.pack()

        frame = ttk.Frame(self)

        menu = tk.Menu(self)
        self.config(menu = menu)
        menubar = tk.Menu(menu)
        menubar.add_command(label='MostrarFrame1',
            command=self.mostrar1)
        menubar.add_command(label='MostrarFrame2',
            command=self.mostrar2)
        menu.add_cascade(label="File",
            menu=menubar)

    def button_clicked():
        return 0
    def mostrar1(event):
        frame1.pack(padx = 10, pady = 0, fill = "x", expand = True)
        frame2.pack_forget()
        return 0
    def mostrar2(event):
        frame2.pack(padx = 10, pady = 0, fill = "x", expand = True)
        frame1.pack_forget()
        return 0
        
def criarFrame1():
    frame = ttk.Frame(app)

    nome = ttk.Label(frame, text = "Nome: ")
    sexo = ttk.Label(frame, text = "Sexo: ")
    data = ttk.Label(frame, text = "Data de Nascimento: ")
    end = ttk.Label(frame, text = "Endereço: ")
    email = ttk.Label(frame, text = "Email: ")

    nomeS = tk.StringVar()
    sexoS = tk.StringVar()
    dataS = tk.StringVar()
    endS = tk.StringVar()
    emailS = tk.StringVar()

    nomeEntrada = ttk.Entry(frame, textvariable = nomeS)
    sexoEntrada = ttk.Entry(frame, textvariable = sexoS)
    dataEntrada = ttk.Entry(frame, textvariable = dataS)
    endEntrada = ttk.Entry(frame, textvariable = endS)
    emailEntrada = ttk.Entry(frame, textvariable = emailS)

    nome.pack( expand = True, pady = 10, side = tk.TOP, anchor = tk.CENTER)
    nomeEntrada.pack( expand = True, side = tk.TOP, anchor = tk.CENTER, ipadx = 50)

    sexo.pack( expand = True, pady = 10, side = tk.TOP, anchor = tk.CENTER)
    sexoEntrada.pack( expand = True, side = tk.TOP, anchor = tk.CENTER, ipadx = 50)

    data.pack( expand = True, pady = 10, side = tk.TOP, anchor = tk.CENTER)
    dataEntrada.pack(expand = True, side = tk.TOP, anchor = tk.CENTER, ipadx = 50)

    end.pack( expand = True, pady = 10, side = tk.TOP, anchor = tk.CENTER)
    endEntrada.pack(expand = True, side = tk.TOP, anchor = tk.CENTER, ipadx = 50)

    email.pack( expand = True, pady = 10, side = tk.TOP, anchor = tk.CENTER)
    emailEntrada.pack( expand = True, side = tk.TOP, anchor = tk.CENTER, ipadx = 50)

    button = ttk.Button(frame, text = "Pesquisar", command = app.destroy)
    button.pack( expand = True, pady = 25, anchor = tk.CENTER)
    return frame


if __name__ == "__main__":
    app = App()
    frame1 = criarFrame1()
    frame2 = criarFrame()
    app.mainloop()
