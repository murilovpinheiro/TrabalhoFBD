from tkinter import *
from  tkinter import ttk
import visualizar as vsz
import alterar as alt
import remover as rmc
import inserir as ins
import pesquisar as psq
import tabelas
import querys as qrs

class App(Tk): #App eh uma subclasse de Tk
    def __init__(self):
        super().__init__()
        #construtor de app que chama o construtor de Tk
        self.title("Tela1")
        self.geometry("1800x1600")

        classes = self.inicializarClasses()
        querys = self.inicializarQuerys()
        self.createMenu(classes, querys)

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
        turma = tabelas.Turma()
        endereco = tabelas.Endereco()
        notas = tabelas.Notas()
        cursos_alunos = tabelas.Cursos_Alunos()
        centro = tabelas.Centro()
        campus = tabelas.Campus()
        reitor = tabelas.Reitor()
        local = tabelas.Local()
        classes = ((aluno, "Aluno"),
                   (prof, "Professor"),
                   (curso, "Curso"),
                   (disc, "Disciplina"),
                   (atd, "Aluno_turma_disc"),
                   (turma, "Turma"),
                   (endereco, "Endereco"),
                   (notas, "Notas"),
                   (cursos_alunos, "Cursos_alunos"),
                   (centro, "Centro"),
                   (campus, "Campus"),
                   (reitor, "Reitor"),
                   (local, "Local"))
        return classes
    
    def inicializarQuerys(self):
        turma_sem = qrs.Turma_Semestre()
        media_turma = qrs.Media_Turma()
        local_bloco = qrs.Local_Bloco()
        turma_local = qrs.Turma_Local()
        media_aluno = qrs.Media_Aluno()
        querys = ((turma_sem, "Turma por Semestre"),
                  (media_turma, "Médias da Turma"),
                  (local_bloco, "Locais por Bloco"),
                  (turma_local, "Turmas por Local"),
                  (media_aluno, "Médias de um Aluno"))
        return querys


    def createMenu(self, classes, querys):
        menu = Menu(self)
        self.config(menu = menu)
        for classe in classes:
            self.createMenuBar(menu, classe[0], classe[1])
        bar = Menu(menu)
        for query in querys:
            self.createPesquisas(bar, query)
        menu.add_cascade(label='Pesquisas', menu=bar)

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
                    ('Pesquise na tabela ' + nome + ' pelo identificador da tabela: ',
                    classe.select, nome), classe.colunas, classe.labels, classe.tipos))
            bar.add_command(label = 'Remover', 
                    command= lambda : self.selecionarRemocao("Digite o identificador da tabela "+ nome + " que deseja remover: ", framePrincipal,
                    classe.delete, classe.select))
            menu.add_cascade(label=nome,
                    menu=bar)
    
    def createPesquisas(self, bar, query):
        bar.add_command(label = query[1], command= lambda : self.selecionarPesquisa(framePrincipal, query[0].label, query[0].codigo, query[0].colunasView, query[0].agrupamento))
        


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
        frameForm.pack( padx = 10, pady = 0, fill = "x", expand = True, anchor = CENTER, side = BOTTOM)
        classe = alt.Alteracao(valores[0], antigo, frameForm, valores[1], valores[2], names, colunas, tipos)
        classe.createSearch()
        classe.pack()
    
    def selecionarRemocao(event, label,antigo,codigo, codigoPesq):
        for widget in antigo.winfo_children():
            widget.destroy()
        classe = rmc.Remocao(label, antigo, codigo, codigoPesq)
        classe.createDelete()
        classe.pack()
    
    def selecionarPesquisa(event, antigo, label, comando, colunas, agrupamento):
        for widget in antigo.winfo_children():
            widget.destroy()
        frameTable = ttk.Frame(antigo)
        frameTable.pack(padx = 10, pady = 0, fill = "x", expand = True, anchor = CENTER, side = BOTTOM)
        classe = psq.Pesquisa(label, antigo, frameTable, comando, colunas, agrupamento)
        classe.createSearch()
        classe.pack()

        
if __name__ == "__main__":
    app = App()
    framePrincipal = ttk.Frame(app)
    label = Label(framePrincipal, text = "PAGINA INICIAL")
    label.pack(padx = 10, pady = 0, fill = "x", expand = True)
    framePrincipal.pack()
    app.mainloop()

