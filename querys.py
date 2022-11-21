class Turma_Semestre():
    def __init__(self):
        self.label = "Digite o Semestre da Turma para Pesquisa: "
        self.codigo = 'select t.*, d.dia_segunda, d.dia_terca, d.dia_quarta, d.dia_quinta, d.dia_sexta from turma t, dias_semana_turma d where t.dias_semana = d.id and t.semestre ='
        self.agrupamento = ""
        self.colunasView = (('ID', 60), ('Estado', 80), ('Quantidade de Alunos', 120),
                            ('Vagas', 100), ('Hora Inicial', 80), ('Hora Final', 80),
                            ('ID da Disciplina', 80), ('Ano e Semestre', 120), ('ID do Local', 80), ('ID do Dias da Semana: ', 120),
                            ('Aula Segunda', 80), ('Aula Terça', 80), ('Aula Quarta', 80), ('Aula Quinta', 80), ('Aula Sexta', 80))

class Media_Turma():
    def __init__(self):
        self.label = "Digite o ID da Turma: "
        self.codigo = "SELECT aux.matr_aluno, aux.media FROM (SELECT atd.matr_aluno, atd.id_disc, atd.id_turma, AVG(n.valor) as media FROM notas n, aluno_turma_disc atd, turma t WHERE n.id_disc = atd.id_disc AND t.id = atd.id_turma AND atd.matr_aluno = n.matr_aluno AND t.estado = 'FECHADA' GROUP BY (atd.matr_aluno, atd.id_disc, atd.id_turma)) aux WHERE aux.id_turma = "
        self.agrupamento = ""
        self.colunasView = (('Matrícula', 80), ('Média', 80))

class Local_Bloco():
    def __init__(self):
        self.label = "Digite o código do Bloco: "
        self.codigo = "SELECT * FROM local WHERE bloco = "
        self.agrupamento = ""
        self.colunasView = (('Código', 80), ('Nome', 120), ('Bloco', 80), ('Lotação', 120), ('Descrição', 160), ('Tipo', 50))

class Turma_Local():
    def __init__(self):
        self.label = "Digite o código do Local: "
        self.codigo = "SELECT d.nome as disciplina_nome, t.id as turma_id, CONCAT(t.horaini, ' - ', t.horafim) as horario_aula FROM turma t, local l, disciplina d WHERE d.id = t.disciplina_id AND t.local_id = l.codigo AND t.local_id = "
        self.agrupamento = ""
        self.colunasView = (("Nome da Disciplina", 140), ("ID da Turma", 120), ("Horário", 160))

class Media_Aluno():
    def __init__(self):
        self.label = "Digite a Matrícula do Aluno: "
        self.codigo = "SELECT d.nome as disciplina, AVG(n.valor) as media FROM notas n, disciplina d WHERE d.id = n.id_disc AND matr_aluno = "
        self.agrupamento = "GROUP BY d.nome"
        self.colunasView = (("Nome Disciplina", 120), ("Média", 100),)


# SELECT d.nome as disciplina_nome, t.id as turma_id, CONCAT(t.horaini, ' - ', t.horafim) as horario_aula FROM turma t, local l, disciplina d WHERE d.id = t.disciplina_id AND t.local_id = l.codigo AND t.local_id = 

