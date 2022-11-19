from tkinter import *
from  tkinter import ttk
import conect as cnt

class Visualizar(ttk.Frame):
    def __init__(self, columns, local, comando):
        super().__init__(local)
        self.columns = columns 
        self.comando = comando
        self.valores = self.consultar()
        self.pack()

    def consultar(self):
        conn = cnt.conectar()
        cur = conn.cursor()
        cur.execute(self.comando)
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return resultado

    def createTable(self):
        scroll = ttk.Scrollbar(self)
        scroll.pack(side = RIGHT, fill = Y)

        table = ttk.Treeview(self, yscrollcommand = scroll.set)
        table.bind('<Button-1>', disableEvent)
        table.bind('<Key>', teste)
        table.pack(fill = BOTH, expand=True)

        scroll.configure(command=table.yview)
        
        columns = []
        table.column("#0", width = 0, stretch = NO)
        for i in range(len(self.columns)):
            columns.append(self.columns[i][0]) 
        table['columns'] = columns
        for i in range(len(self.columns)):
            table.column(self.columns[i][0], anchor = CENTER, width = self.columns[i][1], minwidth= 80)
            table.heading(self.columns[i][0], text = self.columns[i][0], anchor = CENTER)
        for i in range(len(self.valores)):
            table.insert(parent = "", index = "end", iid = i, text = '', values = self.valores[i])

def disableEvent(event):
    return "break"
def teste(event):
    pass
