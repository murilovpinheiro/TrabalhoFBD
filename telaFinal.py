from tkinter import *
from  tkinter import ttk
import insercao as ins
import telaPesquisaAluno as vsz
import alteracaoDinamica as alt
import remocao as rmc


labelsAluno = ('Matricula: ','Nome: ', 'Sexo: ', 'Data de Nascimento: ',
               'Endereço: ', 'Email: ')
colunasViewAluno = (("Matrícula", 80),("Nome", 80), ("Sexo", 80), ("Data Nascimento", 140), ("Endereco", 80), ("Email", 80))
colunasAluno = ('matricula', 'nome', 'sexo', 'data_nasc', 'endereco', 'email')
tiposAluno = ('int', 'str', 'str', 'str', 'int', 'str')

labelsProf = ('ID: ', 'Nome: ', 'Grau de Escolaridade Máxima(G, L, M, D, P): ', 'Sexo: ', 'Data Nascimento: ', 'ID do Curso que Coordena: ', 'ID do Centro que Dirige: ')
colunasViewProf = (("ID", 50), ("Nome", 80), ("Grau de Escolaridade", 140), ("Sexo",80), ("Data Nascimento", 140), ("Curso Coordenado", 140), ("Centro Dirigido", 100))
tiposProf = ('int', 'str', 'str', 'str', 'str', 'int', 'int')
colunasProf = ('id', 'nome', 'grau_max', 'sexo', 'data_nasc', 'coord_curso_id', 'diretor_centro_id')

class App(Tk): #App eh uma subclasse de Tk
    def __init__(self):
        super().__init__()
        #construtor de app que chama o construtor de Tk
        self.title("Tela1")
        self.geometry("1200x800")

        menu = Menu(self)
        self.config(menu = menu)
        alunobar = Menu(menu)
        alunobar.add_command(label='Visualizar',
            command= lambda : self.selecionarVisualizar(framePrincipal,
             colunasViewAluno, "select * from aluno"))
        alunobar.add_command(label='Inserir',
            command= lambda : self.selecionarInsercao(framePrincipal,
             (labelsAluno, {}, "INSERT INTO aluno(matricula, nome, sexo, data_nasc, endereco, email) values "), tiposAluno))
        alunobar.add_command(label = 'Atualizar',
            command= lambda : self.selecionarAlteracao(framePrincipal,
             ('Pesquise um aluno Pela Matrícula: ',
             'select * from aluno where matricula = ', 'aluno'), colunasAluno, labelsAluno))
        alunobar.add_command(label = 'Remover', 
            command= lambda : self.selecionarRemocao("Digite a Matrícula do Aluno que deseja remover: ", framePrincipal,
             "Delete from aluno where matricula = "))
        menu.add_cascade(label="Aluno",
            menu=alunobar)

        profbar = Menu(menu)
        profbar.add_command(label='Visualizar',
            command= lambda : self.selecionarVisualizar(framePrincipal,
            colunasViewProf, "select * from professor"))
        profbar.add_command(label='Inserir',
            command= lambda : self.selecionarInsercao(framePrincipal,
             (labelsProf, {}, "INSERT INTO professor(id, nome, grau_max, sexo, data_nasc, coord_curso_id, diretor_centro_id) values "), tiposProf))
        profbar.add_command(label = 'Atualizar',
            command= lambda : self.selecionarAlteracao(framePrincipal,
             ('Pesquise um Professor Pelo ID: ',
             'select * from professor where id = ', 'professor'), colunasProf, labelsProf, tiposProf))
        profbar.add_command(label = 'Remover', 
            command= lambda : self.selecionarRemocao("Digite ID do Professor que deseja remover: ", framePrincipal,
             "Delete from professor where id = "))
        menu.add_cascade(label="Professor",
        menu=profbar)

        

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
