from tkinter import *
from  tkinter import ttk
from tkinter.messagebox import showinfo
import conectar as cnt
import psycopg2 as psc

class Insercao(ttk.Frame):
    def __init__(self, labels, entrys, local, comando, tipos):
        super().__init__(local)
        self.labels = labels
        self.entrys = entrys
        self.comando = comando
        self.tipos = tipos
        self.pack()

    def createForm(self):
        
        for name in self.labels:
            lb = ttk.Label(self, text = name)
            e = ttk.Entry(self)
            self.entrys[name] = e
            lb.pack( expand = True, pady = 10, side = TOP, anchor = CENTER)
            e.pack( expand = True, side = TOP, anchor = CENTER, ipadx = 50)
        button = ttk.Button(self, text = "Pesquisar", command = self.inserir)
        button.pack( expand = True, pady = 25, anchor = CENTER)

    def inserir(self):
        string = ''
        for i in range(len(self.entrys)):
            if (self.entrys[self.labels[i]].get()) == '':
                string = string + 'NULL'
            elif self.tipos[i] == 'int':
                string = string +self.entrys[self.labels[i]].get()
            else:
                string = string + "'" +self.entrys[self.labels[i]].get()+ "'"
            if i == len(self.labels) - 1:
                break
            string = string + ","
        string = self.comando + "(" + string + ");"
        conn = cnt.conectar()
        cursor = conn.cursor()
        try:
            cursor.execute(string)
            conn.commit()
            showinfo("Aviso", "Salvou")
        except Exception as e:
            showinfo("ERRO",("Dados Digitados são Inválidos: \n", e))
            if (str(e).find("invalid input syntax for type integer") )> -1:
                print("Valor Digitado Inválido")
        cursor.close()
        conn.close()


# if __name__ == "__main__":
#     app = Tk()
#     names = ('Nome: ', 'Sexo: ', 'Data de Nascimento: ',
#             'Endereço: ', 'Email: ')
#     classe = Insercao(names, {}, app,
#     "INSERT INTO aluno(nome, sexo, data_nasc, endereco, email) values ")
#     classe.createForm()
#     app.mainloop()
# EXEMPLO DE MAIN PARA FUNCIONAR