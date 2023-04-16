from tkinter import *
from  tkinter import ttk
from tkinter.messagebox import showinfo
import comandos.conect as cnt

class Pesquisa(ttk.Frame):
    def __init__(self, labelPrincipal ,local, localTable, comando, columns, agrupamento):
        #exemplo: lp = Digite o ID da Turma
        #comando = select * from turma where ID = blabla
        #columns é o columns view
        super().__init__(local)
        self.labelPrincipal = labelPrincipal
        self.local = local
        self.localTable = localTable
        self.comando = comando
        self.agrupamento = agrupamento
        self.columns = columns
        self.valor = 0
        self.pack()

    
    def createSearch(self):
        lb = ttk.Label(self.local, text = self.labelPrincipal)
        e = ttk.Entry(self.local)
        lb.pack( expand = True, pady = 10, side = TOP, anchor = CENTER)
        e.pack( expand = True, side = TOP, anchor = CENTER, ipadx = 60)
        button = ttk.Button(self.local, text = "Pesquisar", command = lambda: self.pesquisar(e))
        button.pack(expand = True, pady = 15, anchor = CENTER)


    def pesquisar(self, e):
        for widget in self.localTable.winfo_children():
            widget.destroy()
        self.valor = e.get()
        if self.valor != "":
            conn = cnt.conectar()
            cursor = conn.cursor()
            string = self.comando + "'" + self.valor + "'" + self.agrupamento
            print(string)
            cursor.execute(string)
            resultado = cursor.fetchall()
            cursor.close()
            conn.close()
            if resultado == []:
                showinfo("ERRO","Valor Não Encontrado\n")
                for widget in self.localTable.winfo_children():
                    widget.destroy()
            else:
                self.createTable(resultado)
        else:
            showinfo("ERRO","Digite um Valor\n")
            for widget in self.localTable.winfo_children():
                widget.destroy()

    def createTable(self, resultado):
        scroll = ttk.Scrollbar(self.localTable)
        scroll.pack(side = RIGHT, fill = Y)

        table = ttk.Treeview(self.localTable, yscrollcommand = scroll.set, height = 5)
        # table.bind('<Button-1>', disableEvent)
        # table.bind('<Key>', teste)
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
        for i in range(len(resultado)):
            table.insert(parent = "", index = "end", iid = i, text = '', values = resultado[i])


# if __name__ == "__main__":
#     root = Tk()
#     root.title("Tela Dinamica")
#     root.geometry("800x600")
#     root.resizable(False, False)

#     framePesq = Frame(root)
#     framePesq.pack(padx = 10, pady = 0, fill = "x")
#     frameForm = Frame(root)
#     frameForm.pack(padx = 10, pady = 0, fill = "x", side = TOP)
#     names = ('Matricula: ','Nome: ', 'Sexo: ', 'Data de Nascimento: ',
#             'Endereço: ', 'Email: ')
#     colunas = (("Matrícula", 80),("Nome", 80), ("Sexo", 80), ("Data Nascimento", 140), ("Endereco", 80), ("Email", 80))
#     nome = "Pesquise um Aluno pela Matrícula: "
#     classe = Pesquisa(nome, framePesq, frameForm, "select * from aluno where matricula = ", colunas)
#     classe.createSearch()
#     root.mainloop()
# #