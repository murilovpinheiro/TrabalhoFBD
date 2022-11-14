from tkinter import *
from  tkinter import ttk
import psycopg2 as psc


def conectar():
    conn = psc.connect(host = "200.129.44.249",
                       database = "510613",
                       user = "510613",
                       password = "510613@fbd")
    return conn

def consultar():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("select nome, sexo, data_nasc, endereco, email from aluno")
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado

def disableEvent(event):
    return "break"
def teste(event):
    pass

def createTable(titulosTamanhos, valores, local):
    scroll = ttk.Scrollbar(local)
    scroll.pack(side = RIGHT, fill = Y)

    table = ttk.Treeview(local, yscrollcommand = scroll.set)
    table.bind('<Button-1>', disableEvent)
    table.bind('<Key>', teste)
    table.pack(fill = BOTH, expand=True)

    scroll.configure(command=table.yview)
    
    columns = []
    table.column("#0", width = 0, stretch = NO)
    for i in range(len(titulosTamanhos)):
        columns.append(titulosTamanhos[i][0]) 
    table['columns'] = columns
    for i in range(len(titulosTamanhos)):
        table.column(titulosTamanhos[i][0], anchor = CENTER, width = titulosTamanhos[i][1], minwidth= 80)
        table.heading(titulosTamanhos[i][0], text = titulosTamanhos[i][0], anchor = CENTER)
    for i in range(len(valores)):
        table.insert(parent = "", index = "end", iid = i, text = '', values = valores[i])



lista = [["Nome", 80], ["Sexo", 80], ["Data Nascimento", 140], ["Endereco", 80], ["Email", 80]]
valores = consultar()
root = Tk()
root.title("Tabela Aluno")
root.geometry("600x300")
root.resizable(False, False)
frame = ttk.Frame(root)
frame.pack(fill = BOTH, expand= True)
createTable(lista, valores, frame)
mainloop()