class Aluno():
    def __init__(self):
        self.labels = ('Matricula: ','Nome: ', 'Sexo: ', 'Data de Nascimento: ',
                       'Endereço: ', 'Email: ')
        self.colunasView = (("Matrícula", 80),("Nome", 80), ("Sexo", 80), ("Data Nascimento", 140), ("Endereco", 80), ("Email", 80), ("Rua", 80), ("Casa", 80))
        self.colunas = ('matricula', 'nome', 'sexo', 'data_nasc', 'endereco', 'email')
        self.tipos = ('int', 'str', 'str', 'str', 'int', 'str')

        self.insert = "INSERT INTO aluno(matricula, nome, sexo, data_nasc, endereco, email) values "
        self.delete = "Delete from aluno where matricula = "
        self.selectAll = "SELECT a.*, e.rua, e.casa FROM aluno a, endereco e WHERE a.endereco = e.id;"
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
        self.labels =  ('ID: ', 'Estado(ABERTA ou FECHADA): ', 'Quantidade de Alunos: ',
                             'Vagas: ','Hora Inicial: ', 'Hora Final: ',
                             'ID da Disciplina: ', 'Ano e Semestre (Formato AAAA.S): ', 'ID do Local: ',
                             'ID dos Dias da Semana: ')
        self.colunasView = (('ID', 60), ('Estado', 120), ('Quantidade de Alunos', 120),
                            ('Vagas', 100), ('Hora Inicial', 80), ('Hora Final', 80),
                            ('ID da Disciplina', 80), ('Ano e Semestre', 120), ('ID do Local', 80), ('Dias da Semana', 80),
                            ('Aula Segunda', 80), ('Aula Terça', 80), ('Aula Quarta', 80), ('Aula Quinta', 80), ('Aula Sexta', 80))
        self.colunas = ('id', 'estado', 'qnt_alunos', 'vagas',
                        'horaini','horafim', 'disciplina_id', 'semestre', 'local_id',
                        'dias_semana')
        self.tipos = ('int', 'str', 'int', 'int', 'int', 'int', 'int', 'sem', 'int', 'int')

        self.insert = 'insert into turma (id, estado, qnt_alunos, vagas, horaini, horafim, disciplina_id, semestre, local_id, dias_semana) values'
        self.delete = 'delete from turma where id = '
        self.selectAll = 'select t.*, d.dia_segunda, d.dia_terca, d.dia_quarta, d.dia_quinta, d.dia_sexta from turma t, dias_semana_turma d where t.dias_semana = d.id'
        self.select = 'select * from turma where id = '

class Endereco():
    def __init__(self):
        self.labels = ('ID: ', 'Rua: ', 'Casa: ', 'Cidade: ', 'Bairro: ', 'Complemento: ')
        self.colunasView = (('ID', 100), ('Rua', 120), ('Casa', 80), ('Cidade', 140), ('Bairro', 140), ('Complemento', 120))
        self.colunas = ('id', 'rua', 'casa', 'cidade', 'bairro', 'complemento')
        self.tipos = ('int', 'str', 'str', 'str', 'str', 'str')

        self.insert = 'insert into endereco(id, rua, casa, cidade, bairro, complemento) values'
        self.delete = 'delete from endereco where id = '
        self.selectAll = 'select * from endereco'
        self.select = 'select * from endereco where id = '

class Notas():
    def __init__(self):
        self.labels = ('ID: ', 'Valor: ', 'Matrícula do Aluno: ', 'ID da Disciplina: ')
        self.colunasView = (('ID', 60), ('Valor', 100), ('Matrícula do Aluno', 160), ('ID da Disciplina', 160))
        self.colunas = ('id', 'valor', 'matr_aluno', 'id_disc')
        self.tipos = ('int', 'int', 'int', 'int')

        self.insert = 'insert into notas(id, valor, matr_aluno, id_disc) values '
        self.delete = 'delete from notas where id = '
        self.selectAll = 'select * from notas'
        self.select = 'select * from notas where id = '

class Cursos_Alunos():
    def __init__(self):
        self.labels = ('ID:', 'Matrícula do Aluno: ', 'ID do Curso: ')
        self.colunasView = (('ID', 80),('Matrícula do Aluno', 160), ('ID do Curso', 160))
        self.colunas = ('id','matr_aluno', 'id_curso')
        self.tipos = ('int', 'int','int')

        self.insert = 'INSERT INTO cursos_alunos(id, matr_aluno, id_curso) values'
        self.delete = 'DELETE FROM cursos_alunos WHERE id = '
        self.selectAll = 'SELECT * FROM cursos_alunos' 
        self.select = 'SELECT * FROM cursos_alunos WHERE id = '

class Centro():
    def __init__(self):
        self.labels = ('ID: ', 'Nome do Centro: ', 'ID do Campus: ', 'ID do Diretor: ')  
        self.colunasView = (('ID', 60), ('Nome do Centro', 160), ('ID do Campus', 160), ('ID do Diretor', 160))
        self.colunas = ('id', 'nome', 'id_campus', 'id_diretor')
        self.tipos = ('int', 'str', 'int', 'int')

        self.insert = 'INSERT INTO centro(id, nome, id_campus, id_diretor) values'
        self.delete = 'DELETE FROM centro WHERE id = '
        self.selectAll = 'SELECT * FROM centro' 
        self.select = 'SELECT * FROM centro WHERE id = '

class Campus():
    def __init__(self):
        self.labels = ('ID: ', 'Nome do Campus: ', 'Local: ', 'ID do Reitor: ') 
        self.colunasView = (('ID', 60), ('Nome do Campus', 160), ('Local', 140), ('ID do Reitor', 160))
        self.colunas = ('id', 'nome', 'localidade', 'id_reitor')
        self.tipos = ('int', 'str', 'str', 'int')

        self.insert = 'INSERT INTO campus(id, nome, localidade, id_reitor) values'
        self.delete = 'DELETE FROM campus WHERE id = '
        self.selectAll = 'SELECT * FROM campus' 
        self.select = 'SELECT * FROM campus WHERE id = '

class Reitor():
    def __init__(self):
        self.labels = ('ID: ', 'Nome do Reitor: ', 'Data de nascimento: ', 'Data de admissão: ', 'ID do Professor: ') 
        self.colunasView = (('ID', 60), ('Nome do Reitor', 160), ('Data de nascimento', 180), ('Data de admissão', 160), ('ID do Professor', 160))
        self.colunas = ('codigo', 'nome', 'data_nasc', 'data_adm', 'id_professor')
        self.tipos = ('int', 'str', 'str', 'str', 'int')

        self.insert = 'INSERT INTO reitor(codigo, nome, data_nasc, data_adm, id_professor) values'
        self.delete = 'DELETE FROM reitor WHERE codigo = '
        self.selectAll = 'SELECT * FROM reitor' 
        self.select = 'SELECT * FROM reitor WHERE codigo = '

class Local():
    def __init__(self):
        self.labels =  ('ID: ', 'Nome do Local: ', 'ID do Bloco: ', 'Lotação do Local: ', 'Descrição do Local: ', 'Tipo do Local: ')
        self.colunasView = (('ID', 60), ('Nome do Local', 160), ('ID do Bloco', 160), ('Lotacao do Local', 160), ('Descrição do Local', 200), ('Tipo do Local', 160))
        self.colunas = ('codigo', 'nome', 'bloco', 'lotacao', 'descricao', 'tipo')
        self.tipos = ('int', 'str', 'int', 'int', 'str', 'str')

        self.insert = 'INSERT INTO local(codigo, nome, bloco, lotacao, descricao, tipo) values'
        self.delete = 'DELETE FROM local WHERE codigo = '
        self.selectAll = 'SELECT * FROM local' 
        self.select = 'SELECT * FROM local WHERE codigo = '

class Dias_Semana_Turma():
    def __init__(self):
        self.labels =  ('ID: ', 'Tem aula Segunda? (SIM ou NÃO)', 'Tem aula Terça? (SIM ou NÃO)','Tem aula Quarta? (SIM ou NÃO)',
                                'Tem aula Quinta? (SIM ou NÃO)','Tem aula Sexta? (SIM ou NÃO)')
        self.colunasView = (('ID', 60), ('Aula Segunda', 100), ('Aula Terça', 100), ('Aula Quarta', 100), ('Aula Quinta', 100),('Aula Sexta', 100))
        self.colunas = ('id', 'dia_segunda', 'dia_terca', 'dia_quarta', 'dia_quinta', 'dia_sexta')
        self.tipos = ('int', 'str', 'str', 'str', 'str', 'str')

        self.insert = 'INSERT INTO dias_semana_turma(id, dia_segunda, dia_terca, dia_quarta, dia_quinta, dia_sexta) values'
        self.delete = 'DELETE FROM dias_semana_turma WHERE id = '
        self.selectAll = 'SELECT * FROM dias_semana_turma' 
        self.select = 'SELECT * FROM dias_semana_turma WHERE id = '