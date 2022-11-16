from tkinter import *
from  tkinter import ttk
from tkinter.messagebox import showinfo
import conectar as cnt

class Alteracao(ttk.Frame):
    def __init__(self, labelPrincipal, local, localForm, codigoPesq, tabela, labels, colunas, tipos):
        super().__init__(local)
        self.labelPrincipal = labelPrincipal
        self.local = local
        self.localForm = localForm
        self.codigoPesq = codigoPesq
        self.tabela = tabela
        self.labels = labels
        self.colunas = colunas
        self.entrys = {}
        self.tipos = tipos
        self.valor = 0
        self.pack()

    
    def createSearch(self):
        lb = ttk.Label(self.local, text = self.labelPrincipal)
        e = ttk.Entry(self.local)
        lb.pack( expand = True, pady = 10, side = TOP, anchor = CENTER)
        e.pack( expand = True, side = TOP, anchor = CENTER, ipadx = 50)
        button = ttk.Button(self.local, text = "Pesquisar", command = lambda: self.pesquisar(e))
        button.pack(expand = True, pady = 25, anchor = CENTER)


    def pesquisar(self, e):
        self.valor = e.get()
        if self.valor != "":
            conn = cnt.conectar()
            cursor = conn.cursor()
            string = self.codigoPesq + self.valor
            print(string)
            cursor.execute(string)
            resultado = cursor.fetchall()
            cursor.close()
            conn.close()
            if resultado == []:
                showinfo("ERRO","Valor Não Encontrado\n")
                for widget in self.localForm.winfo_children():
                    widget.destroy()
            else:
                self.createForm(resultado, e.get())
        else:
            showinfo("ERRO","Digite um Valor\n")
            for widget in self.localForm.winfo_children():
                widget.destroy()
            


    def createForm(self, resultado, pk):
        for widget in self.localForm.winfo_children():
                widget.destroy()
        i = 0
        for label in self.labels:
            lb = ttk.Label(self.localForm, text = label)
            e = ttk.Entry(self.localForm)
            self.entrys[label] = e
            lb.pack( expand = True, pady = 10, side = TOP, anchor = CENTER)
            e.pack( expand = True, side = TOP, anchor = CENTER, ipadx = 50)
            if resultado[0][i] != None:
                e.insert(END, resultado[0][i])
            i+=1
        button = ttk.Button(self.localForm, text = "Pesquisar", command = lambda : self.atualizar(pk))
        button.pack( expand = True, pady = 25, anchor = CENTER)

    def atualizar(self, pk):
        string = ''
        for i in range(len(self.colunas)):
            print(self.entrys[self.labels[i]].get(), ' ')
            if self.entrys[self.labels[i]].get() == '':
                string = string + self.colunas[i] + " = " + "NULL"
            elif self.tipos[i] == 'int':
                string = string + self.colunas[i] + " = " + self.entrys[self.labels[i]].get()
            else:
                string = string + self.colunas[i] + " = " + "'" + self.entrys[self.labels[i]].get() + "'"
            if i == len(self.colunas) - 1:
                #pra nao colocar virgula no final
                string = string + " where " +  self.colunas[0] + " = " + pk
                break
            string = string + ", "
        string = "UPDATE " + self.tabela + " SET " + string
        print(string)
        conn = cnt.conectar()
        cursor = conn.cursor()
        try:
            cursor.execute(string)
            conn.commit()
            showinfo("Aviso: ", "Salvou")
        except Exception as e:
            showinfo("ERRO",("Dados Digitados são Inválidos: \n %e", e))
        cursor.close()
        conn.close()

# if __name__ == "__main__":
#     root = Tk()
#     root.title("Tela Dinamica")
#     root.geometry("800x600")
#     root.resizable(False, False)


#     framePesq = Frame(root)
#     framePesq.pack(padx = 10, pady = 0, fill = "x", expand = True)
#     frameForm = Frame(root)
#     frameForm.pack(padx = 10, pady = 0, fill = "x", expand = True, anchor = CENTER)
#     names = ('Matricula: ','Nome: ', 'Sexo: ', 'Data de Nascimento: ',
#             'Endereço: ', 'Email: ')
#     colunas = ('matricula', 'nome', 'sexo', 'data_nasc', 'endereco', 'email')
#     nome = "Pesquise um pela Matrícula: "
#     classe = Alteracao(nome, framePesq, frameForm, "select * from aluno where matricula = ", "aluno", names, colunas)
#     classe.createSearch()
#     root.mainloop()
##
        # names = ('Nome: ', 'Sexo: ', 'Data de Nascimento: ',
        #     'Endereço: ', 'Email: '

