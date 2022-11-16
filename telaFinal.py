from tkinter import *
from  tkinter import ttk
import insercao as ins
import telaPesquisaAluno as vsz
import alteracaoDinamica as alt
import remocao as rmc
import tabelas

class App(Tk): #App eh uma subclasse de Tk
    def __init__(self):
        super().__init__()
        #construtor de app que chama o construtor de Tk
        self.title("Tela1")
        self.geometry("1200x800")

        classes = self.inicializarClasses()

        self.createMenu(classes)

        # self.createMenuAluno(menu)
        # self.createMenuProf(menu)
        # self.createMenuDisciplina(menu)
        # self.createMenuCurso(menu)
        # self.createMenuCursoAluno(menu)

    def inicializarClasses(self):
        aluno = tabelas.Aluno()
        prof = tabelas.Professor()
        disc = tabelas.Disciplina()
        curso = tabelas.Curso()
        atd = tabelas.Aluno_turma_disc()
        classes = ((aluno, "Aluno"),
                   (prof, "Professor"),
                   (curso, "Curso"),
                   (disc, "Disciplina"),
                   (atd, "Aluno_turma_disc"))
        return classes
    
    def createMenu(self, classes):
        menu = Menu(self)
        self.config(menu = menu)
        for classe in classes:
            self.createMenuBar(menu, classe[0], classe[1])

    def createMenuBar(self, menu, classe, nome):
            #aluno = tabelas.Aluno()
            bar = Menu(menu)
            bar.add_command(label='Visualizar',
                    command= lambda : self.selecionarVisualizar(framePrincipal,
                    classe.colunasView, classe.selectAll))
            bar.add_command(label='Inserir',
                    command= lambda : self.selecionarInsercao(framePrincipal,
                    (classe.labels, {},classe.insert), classe.tipos))
            bar.add_command(label = 'Atualizar',
                    command= lambda : self.selecionarAlteracao(framePrincipal,
                    ('Pesquise na tabela ' +nome+ ' pelo identificador da tabela: ',
                    classe.select, nome), classe.colunas, classe.labels, classe.tipos))
            bar.add_command(label = 'Remover', 
                    command= lambda : self.selecionarRemocao("Digite o identificador da tabela "+ nome + " que deseja remover: ", framePrincipal,
                    classe.delete))
            menu.add_cascade(label=nome,
                    menu=bar)

    def selecionarVisualizar(event, antigo, lista, comando):
        for widget in antigo.winfo_children():
            widget.destroy()
        classe = vsz.Visualizar(lista, antigo, comando)
        classe.createTable()
        classe.pack()

    def selecionarInsercao(event, antigo, valores, tipos):
        for widget in antigo.winfo_children():
            widget.destroy()
        classe = ins.Insercao(valores[0], valores[1], antigo, valores[2], tipos)
        classe.createForm()
        classe.pack()

    def selecionarAlteracao(event, antigo, valores, colunas, names, tipos):
        for widget in antigo.winfo_children():
            widget.destroy()
        frameForm = ttk.Frame(antigo)
        frameForm.pack( padx = 10, pady = 0, fill = "x", expand = True, anchor = CENTER)
        classe = alt.Alteracao(valores[0], antigo, frameForm, valores[1], valores[2], names, colunas, tipos)
        classe.createSearch()
        classe.pack()
    
    def selecionarRemocao(event, label,antigo,codigo):
        for widget in antigo.winfo_children():
            widget.destroy()
        classe = rmc.Remocao(label, antigo, codigo)
        classe.createDelete()
        classe.pack()
        
if __name__ == "__main__":
    app = App()
    framePrincipal = ttk.Frame(app)
    label = Label(framePrincipal, text = "PAGINA INICIAL")
    label.pack(padx = 10, pady = 0, fill = "x", expand = True)
    framePrincipal.pack()
    app.mainloop()

