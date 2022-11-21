-- INSERTS UTILIZADOS NO PYTHON PARA INSERÇÃO DE VALORES NO BANCO
-- OS VALORES DE INSERÇÃO VÃO DENTRO DOS PARENTESES VAZIOS
    -- TABELA ALUNO:
    INSERT INTO aluno(matricula, nome, sexo, data_nasc, endereco, email) values ()

    -- TABELA PROFESSOR:
    INSERT INTO professor(id, nome, grau_max, sexo, data_nasc, coord_curso_id, diretor_centro_id) values ()

    -- TABELA DISCIPLINA
    INSERT INTO disciplina(id, nome, ementa, carga_hor, professor_id) values ()

    -- TABELA CURSO
    INSERT INTO curso(id, nome, carga_hor, id_centro, id_coord) values ()

    -- TABELA ALUNO_TURMA_DISC
    INSERT INTO aluno_turma_disc( id,matr_aluno, id_disc, id_turma) values ()

    -- TABELA TURMA
    INSERT INTO turma (id, estado, qnt_alunos, vagas, horaini, horafim, disciplina_id, semestre, local_id, dias_semana) values ()

    -- TABELA ENDERECO
    INSERT INTO endereco(id, rua, casa, cidade, bairro, complemento) values ()

    -- TABELA NOTAS
    INSERT INTO notas(id, valor, matr_aluno, id_disc) values ()

    -- TABELA CURSOS_ALUNOS
    INSERT INTO cursos_alunos(id, matr_aluno, id_curso) values ()

    -- TABELA CENTRO
    INSERT INTO centro(id, nome, id_campus, id_diretor) values ()

    -- TABELA CAMPUS
    INSERT INTO campus(id, nome, localidade, id_reitor) values ()

    -- TABELA REITOR
    INSERT INTO reitor(codigo, nome, data_nasc, data_adm, id_professor) values ()

    -- TABELA LOCAL
    INSERT INTO local(codigo, nome, bloco, lotacao, descricao, tipo) values ()

    -- TABELA DIAS_SEMANA_TURMA
    INSERT INTO dias_semana_turma(id, dia_segunda, dia_terca, dia_quarta, dia_quinta, dia_sexta) values ()