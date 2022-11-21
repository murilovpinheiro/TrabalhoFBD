-- OPERAÇÕES DE ATUALIZAÇÃO UTILIZADAS NO PYTHON
-- OS VALORES PREENCHIDOS SÃO VALORES DE EXEMPLO DE OPERAÇÕES BEM SUCEDIDAS PELO PYTHON
    -- TABELA ALUNO
    UPDATE Aluno SET matricula = 11, nome = 'Paulo', sexo = 'O', data_nasc = '1999-12-12', endereco = 3, email = NULL where matricula = 11
    
    -- TABELA PROFESSOR
    UPDATE Professor SET id = 77, nome = 'Julio Alves', grau_max = 'D', sexo = 'M', data_nasc = '1990-01-01', coord_curso_id = NULL, diretor_centro_id = NULL where id = 77
   
    -- TABELA CURSO
    UPDATE Curso SET id = 1, nome = 'Computação', carga_hor = 20, id_centro = 1, id_coord = 1 where id = 1
    
    -- TABELA DISCIPLINA
    UPDATE Disciplina SET id = 1, nome = 'Fundamento', ementa = 'Fundamental', carga_hor = 256, professor_id = 1 where id = 1
    
    -- TABELA ALUNO_TURMA_DISC
    UPDATE Aluno_turma_disc SET id = 1, matr_aluno = 509299, id_disc = 1, id_turma = 1 where id = 1
   
    -- TABELA TURMA
    UPDATE Turma SET id = 4, estado = 'ABERTA', qnt_alunos = 0, vagas = 6, horaini = 10, horafim = 11, disciplina_id = 2, semestre = '2022.2', local_id = 1, dias_semana = 1 where id = 4  
    
    -- TABELA ENDERECO
    UPDATE Endereco SET id = 1, rua = 'lalau', casa = '13', cidade = 'Fortaleza', bairro = 'Bairro1', complemento = NULL where id = 1
  
    -- TABELA NOTAS
    UPDATE Notas SET id = 1, valor = 10.0, matr_aluno = 509299, id_disc = 1 where id = 1
 
    -- TABELA CURSOS_ALUNOS
    UPDATE Cursos_alunos SET id = 1, matr_aluno = 11, id_curso = 1333 where id = 1
 
    -- TABELA CENTRO
    UPDATE Centro SET id = 1, nome = 'centro paia', id_campus = 1, id_diretor = 1 where id = 1
  
    -- TABELA CAMPUS
    UPDATE Campus SET id = 1, nome = 'Campus do Pici', localidade = 'Pici', id_reitor = 1 where id = 1
 
    -- TABELA REITOR
    UPDATE Reitor SET codigo = 1, nome = 'candido', data_nasc = '1950-03-05', data_adm = '2020-03-09', id_professor = 2 where codigo = 1

    -- TABELA LOCAL
    UPDATE Local SET codigo = 1, nome = 'nome1', bloco = NULL, lotacao = 200, descricao = NULL, tipo = 'B' where codigo = 1

    --TABELA DIAS_SEMANA_TURMA
    UPDATE Dias_Semana_Turma SET id = 3, dia_segunda = 'NÃO', dia_terca = 'NÃO', dia_quarta = 'NÃO', dia_quinta = 'NÃO', dia_sexta = 'NÃO' where id = 3