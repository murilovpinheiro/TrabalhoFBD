from tkinter import *
from  tkinter import ttk
from tkinter.messagebox import showinfo
import conectar as cnt

class Remocao(ttk.Frame):
    def __init__(self, labelPrincipal, local, codigo):
        super().__init__(local)
        self.labelPrincipal = labelPrincipal
        self.local = local
        self.codigo = codigo
        self.pack()

    
    def createDelete(self):
        lb = ttk.Label(self.local, text = self.labelPrincipal)
        e = ttk.Entry(self.local)
        lb.pack( expand = True, pady = 10, side = TOP, anchor = CENTER)
        e.pack( expand = True, side = TOP, anchor = CENTER, ipadx = 50)
        button = ttk.Button(self.local, text = "Deletar", command = lambda: self.deletar(e.get()))
        button.pack(expand = True, pady = 25, anchor = CENTER)


    def deletar(self, e):
        if e != "":
            try:
                conn = cnt.conectar()
                cursor = conn.cursor()
                string = self.codigo + e
                print(string)
                cursor.execute(string)
                conn.commit()
                cursor.close()
                conn.close()
                showinfo("AVISO", "Valor deletado com sucesso.\n")
            except:
                showinfo("ERRO", "Valor não encontrado.\n")
        else:
            showinfo("ERRO","Digite um Valor\n")
            cursor.close()
            conn.close()
