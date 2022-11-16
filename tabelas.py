class Aluno():
    def __init__(self):
        self.labels = ('Matricula: ','Nome: ', 'Sexo: ', 'Data de Nascimento: ',
                       'Endereço: ', 'Email: ')
        self.colunasView = (("Matrícula", 80),("Nome", 80), ("Sexo", 80), ("Data Nascimento", 140), ("Endereco", 80), ("Email", 80))
        self.colunas = ('matricula', 'nome', 'sexo', 'data_nasc', 'endereco', 'email')
        self.tipos = ('int', 'str', 'str', 'str', 'int', 'str')

        self.insert = "INSERT INTO aluno(matricula, nome, sexo, data_nasc, endereco, email) values "
        self.delete = "Delete from aluno where matricula = "
        self.selectAll = "select * from aluno"
        self.select = 'select * from aluno where matricula = '

class Professor():
    def __init__(self):
        self.labels = ('ID: ', 'Nome: ', 'Grau de Escolaridade Máxima(G, L, M, D, P): ', 'Sexo: ', 'Data Nascimento: ', 'ID do Curso que Coordena: ', 'ID do Centro que Dirige: ')
        self.colunasView = (("ID", 50), ("Nome", 80), ("Grau de Escolaridade", 140), ("Sexo",80), ("Data Nascimento", 140), ("Curso Coordenado", 140), ("Centro Dirigido", 100))
        self.colunas = ('id', 'nome', 'grau_max', 'sexo', 'data_nasc', 'coord_curso_id', 'diretor_centro_id')
        self.tipos = ('int', 'str', 'str', 'str', 'str', 'int', 'int')

        self.insert = "INSERT INTO professor(id, nome, grau_max, sexo, data_nasc, coord_curso_id, diretor_centro_id) values "
        self.delete = "Delete from professor where id = "
        self.selectAll = "select * from professor"
        self.select = 'select * from professor where id = '

class Disciplina():
    def __init__(self):
        self.labels = ('ID: ', 'Nome da Disciplina: ', 'Ementa da Disciplina: ', 'Carga Horária', 'Professor')
        self.colunasView = (('ID', 50), ('Nome', 80), ('Ementa', 200), ('Carga Horária', 140), ('Professor', 50))
        self.colunas = ('id', 'nome', 'ementa', 'carga_hor', 'professor_id')
        self.tipos = ('int', 'str', 'str', 'int', 'int')

        self.insert = 'INSERT INTO disciplina(id, nome, ementa, carga_hor, professor_id) values'
        self.delete = 'delete from disciplina where id = '
        self.selectAll = 'select * from disciplina'
        self.select = 'select * from disciplina where id = '

class Curso():
    def __init__(self):
        self.labels = ('ID: ', 'Nome: ', 'Carga Horária: ', 'ID do Centro: ', 'ID do Coordenador: ')
        self.colunasView = (('ID', 50), ('Nome', 120), ('Carga Horária', 140), ('ID do Centro', 120), ('ID do Coordenador', 120))
        self.colunas = ('id', 'nome', 'carga_hor', 'id_centro', 'id_coord')
        self.tipos = ('int', 'str', 'int', 'int', 'int')

        self.insert = 'INSERT INTO curso(id, nome, carga_hor, id_centro, id_coord) values'
        self.delete = 'delete from curso where id = '
        self.selectAll = 'select * from curso'
        self.select = 'select * from curso where id = '  

class Aluno_turma_disc():
    def __init__(self):
        self.labels = ('ID: ', 'Matrícula do Aluno: ', 'ID da Disciplina: ', 'ID da Turma: ')
        self.colunasView = (('ID', 60),('Matrícula do Aluno', 120), ('ID da Disciplina', 120), ('ID da Turma', 120))
        self.colunas = ('id','matr_aluno', 'id_disc', 'id_turma')
        self.tipos = ('int', 'int', 'int', 'int')

        self.insert = 'INSERT INTO aluno_turma_disc( id,matr_aluno, id_disc, id_turma) values'
        self.delete = 'delete from aluno_turma_disc where id ='
        self.selectAll = 'select * from aluno_turma_disc'
        self.select = 'select * from aluno_turma_disc where id='

class Turma():
    def __init__(self):
        self.labels =  ('ID: ', 'Estado(1 para Aberta, 0 para Fechada): ', 'Quantidade de Alunos: ',
                             'Vagas: ','Hora Inicial: ', 'Hora Final: ',
                             'ID da Disciplina: ', 'Ano e Semestre (Formato {AAAA.S}): ', 'ID do Local: ')
        self.colunasView = (('ID', 60), ('Estado', 80), ('Quantidade de Alunos', 120),
                             ('Vagas', 100), ('Hora Inicial', 80), ('Hora Final', 80), ('ID da Disciplina', 80), ('Ano e Semestre', 120), ('ID do Local', 80))
        self.colunas = ('id', 'estado', 'qnt_alunos', 'vagas',
                        'horaini','horafim', 'disciplina_id', 'semestre', 'local_id')
        self.tipos = ('int', 'bool', 'int', 'int', 'int', 'int', 'int', 'sem', 'int')

        self.insert = 'insert into turma (id, estado, qnt_alunos, vagas, horaini, horafim, disciplina_id, semestre, local_id ) values'
        self.delete = 'delete from turma where id = '
        self.selectAll = 'select * from turma'
        self.select = 'select * from turma where id = '


        # self.labels = 
        # self.colunasView = 
        # self.colunas = 
        # self.tipos = 

        # self.insert = 
        # self.delete = 
        # self.selectAll = 
        # self.select = 