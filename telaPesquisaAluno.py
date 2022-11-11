from tkinter import *
from  tkinter import ttk

# alunoInfo = ["Nome ", "Sexo ", "Data Nascimento ", "Endereco ", "Email "]
# label = {}

# root = tk.Tk()
# root.geometry("1200x800")
# frame  = ttk.Frame(root)
# frame.grid(padx = 10, pady = 0)
# p = ttk.Label(root, text = "Pesquise um Aluno pela Matricula: ")
# i = 0
# for info in alunoInfo:
#     lb = ttk.Label(frame,font=('Helvetica',12), background = "#e6e6ff" , width = 12,text = info, borderwidth = 1, relief = "solid", anchor = "w")
#     lb.grid(row = 0, column = i)
#     label[info] = lb
#     i+=1
def disableEvent(event):
    return "break"
def teste(event):
    pass

def createTable(titulosTamanhos, valores, local):
    scroll = ttk.Scrollbar(local)
    scroll.pack(side = "bottom", fill = X)

    table = ttk.Treeview(local, xscrollcommand = scroll.set)
    table.bind('<Button-1>', disableEvent)
    table.bind('<Key>', teste)
    table.pack()

    scroll.config(command=table.xview)
    
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
valores = ((1,2,3,4,5), (5,6,7,8,9))
root = Tk()
root.geometry("1200x800")
createTable(lista, valores, root)
mainloop()