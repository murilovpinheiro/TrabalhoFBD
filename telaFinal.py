from tkinter import *
from  tkinter import ttk
import insercao as ins
import telaPesquisaAluno as vsz
import alteracaoDinamica as alt

labelsAluno = ('Matricula: ','Nome: ', 'Sexo: ', 'Data de Nascimento: ',
               'Endereço: ', 'Email: ')
colunasViewAluno = (("Matrícula", 80),("Nome", 80), ("Sexo", 80), ("Data Nascimento", 140), ("Endereco", 80), ("Email", 80))
colunasAluno = ('matricula', 'nome', 'sexo', 'data_nasc', 'endereco', 'email')

class App(Tk): #App eh uma subclasse de Tk
    def __init__(self):
        super().__init__()
        #construtor de app que chama o construtor de Tk
        self.title("Tela1")
        self.geometry("1200x800")

        menu = Menu(self)
        self.config(menu = menu)
        menubar = Menu(menu)
        menubar.add_command(label='Visualizar',
            command= lambda : self.selecionarVisualizar(framePrincipal, colunasViewAluno, "select * from aluno"))
        menubar.add_command(label='Inserir',
            command= lambda : self.selecionarInsercao(framePrincipal, (labelsAluno, {}, "INSERT INTO aluno(matricula, nome, sexo, data_nasc, endereco, email) values ")))
        menubar.add_command(label = 'Atualizar',
            command= lambda : self.selecionarAlteracao(framePrincipal, ('Pesquise um aluno Pela Matrícula: ',
             'select * from aluno where matricula = ', 'aluno'), colunasAluno, labelsAluno))
        menu.add_cascade(label="Aluno",
            menu=menubar)

    def selecionarVisualizar(event, antigo, lista, comando):
        for widget in antigo.winfo_children():
            widget.destroy()
        classe = vsz.Visualizar(lista, antigo, comando)
        classe.createTable()
        classe.pack()

    def selecionarInsercao(event, antigo, valores):
        for widget in antigo.winfo_children():
            widget.destroy()
        classe = ins.Insercao(valores[0], valores[1], antigo, valores[2])
        classe.createForm()
        classe.pack()

    def selecionarAlteracao(event, antigo, valores, colunas, names):
        for widget in antigo.winfo_children():
            widget.destroy()
        frameForm = ttk.Frame(antigo)
        frameForm.pack( padx = 10, pady = 0, fill = "x", expand = True, anchor = CENTER)
        classe = alt.Alteracao(valores[0], antigo, frameForm, valores[1], valores[2], names, colunas)
        classe.createSearch()
        classe.pack()
        
if __name__ == "__main__":
    app = App()
    framePrincipal = ttk.Frame(app)
    label = Label(framePrincipal, text = "PAGINA INICIAL")
    label.pack(padx = 10, pady = 0, fill = "x", expand = True)
    framePrincipal.pack()
    app.mainloop()
