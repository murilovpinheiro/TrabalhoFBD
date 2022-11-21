-- Códigos de Criações das Tabelas
-- OS CHECKS FORAM TODOS ADICIONADOS PÓS CRIAÇÕES DAS TABELAS
--ALUNO
create table aluno(matricula int not null,
				   nome character varying(80) not null,
				   sexo character varying(1) not null,
				   data_nasc date not null,
				   endereco int not null,
				   email character varying(50),
				   primary key(matricula),
				   foreign key (endereco) references endereco);

--PROFESSOR
create table professor(id int not null,
					   nome character varying(80) not null,
					   grau_max character varying(1) not null,
					   sexo character varying(1) not null,
					   data_nasc date not null,
					   coord_curso_id int not null,
					   diretor_centro_id int not null,
					   primary key (id),
					   foreign key (coord_curso_id) references curso,
					   foreign key (diretor_centro_id) references centro);

--DISCIPLINA
create table disciplina(id int not null,
					    nome character varying(100) not null,
					    ementa character varying(200) not null,
					    carga_hor int not null,
					    professor_id int not null,
					    primary key (id),
					    foreign key (professor_id) references professor);

--CURSO
create table curso(id int not null,
				   nome character varying(50) not null,
				   carga_hor int not null,
				   id_centro int not null,
				   id_coord int not null,
				   primary key (id),
				   foreign key (id_centro) references centro,
				   foreign key (id_coord) references professor);

--ALUNO_TURMA_DISC
create table aluno_turma_disc(id int not null,
							  matr_aluno int not null,
							  id_disc int not null,
							  id_turma int not null,
							  primary key (id),
							  foreign key (matr_aluno) references aluno,
							  foreign key (id_disc) references disciplina,
							  foreign key (id_turma) references turma);

--TURMA
create table turma(id int not null,
				   estado character varying(7) not null,
				   qnt_alunos int not null,
				   vagas int not null,
				   horaini int not null,
				   horafim int not null,
				   disciplina_id int not null,
				   semestre character varying(15) not null,
				   local_id int not null,
				   dias_semana int not null,
				   primary key (id),
				   foreign key (disciplina_id) references disciplina,
				   foreign key (local_id) references local,
				   foreign key (dias_semana) references dias_semana_turma);

--ENDERECO
create table endereco(id int not null,
					  rua character varying(50) not null,
					  casa int not null,
					  cidade character varying(50) not null,
					  bairro character varying(50) not null,
					  complemento character varying(50),
					  primary key (id));

--NOTAS
create table notas(id int not null,
				   valor float not null,
				   matr_aluno int not null,
				   id_disc int not null,
				   primary key (id),
				   foreign key (matr_aluno) references aluno,
				   foreign key (id_disc) references disciplina);

--CURSOS_ALUNOS
create table cursos_alunos (id int not null,
						    matr_aluno int not null,
						    id_curso int not null,
						    primary key (id),
						    foreign key (matr_aluno) references aluno,
						    foreign key (id_curso) references curso);
                        
--CENTRO
create table centro (id int not null,
					 nome character varying(80) not null,
					 id_campus int not null,
					 id_diretor int not null,
					 primary key(id),
					 foreign key (id_campus) references campus,
					 foreign key (id_diretor) references professor);

--CAMPUS
create table campus (id int not null,
					 nome character varying(80) not null,
					 localidade character varying(80) not null,
					 id_reitor int not null,
					 primary key (id),
					 foreign key (id_reitor) references reitor);

--REITOR
create table reitor(codigo int not null,
				    nome character varying(80) not null,
				    data_nasc date not null,
				    data_adm date not null,
				    id_professor int not null,
				    primary key (codigo),
				    foreign key (id_professor) references professor);

--LOCAL
create table local (codigo int not null,
				    nome character varying(80) not null,
				    bloco int not null,
				    lotacao int not null,
				    descricao character varying(80) not null,
				    tipo character varying(1) not null,
				    primary key (codigo));

--DIAS_SEMANA_TURMA
create table dias_semana_turma(id int not null,
							   dia_segunda character varying(3) not null,
							   dia_terca character varying(3) not null,
							   dia_quarta character varying(3) not null,
							   dia_quinta character varying(3) not null,
							   dia_sexta character varying(3) not null,
							   primary key (id));


--ALTERAÇÕES NAS TABELAS PARA COLOCAR OS CHECKS QUE UTILIZAMOS
--CHECKS ALUNO:

    ALTER TABLE aluno add check (sexo IN ('o', 'f', 'm', 'O', 'F', 'M'));

    ALTER TABLE aluno add check (data_nasc > '1900-01-01'::date AND data_nasc < now());

    --CHECKS TURMA:

    ALTER TABLE turma add check (estado IN ('ABERTA', 'FECHADA'));

    ALTER TABLE turma add check (hora_ini < hora_fim);

    --CHECKS LOCAL:

    ALTER TABLE local add check (
    upper(tipo::text) = 'B'::text OR
    upper(tipo::text) = 'A'::text OR
    upper(tipo::text) = 'S'::text OR
    upper(tipo::text) = 'L'::text);

--CHECKS NOTA:

    ALTER TABLE notas add check(valor >= 0::double precision AND valor <= 10::double precision);

    --CHECKS PROFESSOR:

    ALTER TABLE professor add check (
    upper(grau_max::text) = 'G'::text OR
    upper(grau_max::text) = 'M'::text OR
    upper(grau_max::text) = 'D'::text OR
    upper(grau_max::text) = 'P'::text OR
    upper(grau_max::text) = 'L'::text);

    ALTER TABLE professor add check (
    lower(sexo::text) = 'm'::text OR
    lower(sexo::text) = 'f'::text OR
    lower(sexo::text) = 'o'::text);

    ALTER TABLE professor add check(data_nasc > '1900-01-01'::date AND data_nasc < now());

    --CHECKS REITOR
    ALTER TABLE reitor add check (data_nasc < now() AND data_nasc < data_adm AND data_adm <= now());

    --CHECKS DIAS_SEMANA_TURMA

    ALTER TABLE dias_semana_turma add check (dia_segunda IN ('SIM', 'NÃO'));

    ALTER TABLE dias_semana_turma add check (dia_terca IN ('SIM', 'NÃO'));

    ALTER TABLE dias_semana_turma add check (dia_quarta IN ('SIM', 'NÃO'));

    ALTER TABLE dias_semana_turma add check (dia_quinta IN ('SIM', 'NÃO'));

    ALTER TABLE dias_semana_turma add check (dia_sexta IN ('SIM', 'NÃO')); 

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

-- COMANDOS DE REMOÇÃO DO BANCO DE DADOS UTILIZADOS NO PYTHON
-- TABELA  ALUNO
    delete from aluno where matricula = 
    -- TABELA PROFESSOR
    delete from professor where id = 
    -- TABELA CURSO
    delete from curso where id = 
    -- TABELA DISCIPLINA
    delete from disciplina where id = 
    -- TABELA ALUNO_TURMA_DISC
    delete from aluno_turma_disc where id =
    -- TABELA TURMA
    delete from turma where id = 
    -- TABELA ENDERECO
    delete from endereco where id = 
    -- TABELA NOTAS
    delete from notas where id = 
    -- TABELA CURSOS_ALUNOS
    delete FROM cursos_alunos WHERE id = 
    -- TABELA CENTRO
    delete FROM centro WHERE id = 
    -- TABELA CAMPUS
    delete FROM campus WHERE id = 
    -- TABELA REITOR
    delete FROM reitor WHERE codigo = 
    -- TABELA LOCAL
    delete FROM local WHERE codigo = 
    -- TABELA DIAS_SEMANA_TURMA
    DELETE FROM dias_semana_turma WHERE id = 


-- SELECTS UTILIZADOS NO PYTHON PARA VISUALIZAÇÃO
    -- TABELA ALUNO:
    SELECT a.*, e.rua, e.casa FROM aluno a, endereco e WHERE a.endereco = e.id; -- TODOS OS VALORES DA TABELA ALUNO ALÉM DOS VALORES DE ENDEREÇO PARA FACILITAR A VISUALIZAÇÃO
    SELECT * FROM aluno WHERE matricula = -- algum valor de matrícula -- PESQUISA DE ALGUM ALUNO PELA MATRÍCULA

    -- TABELA PROFESSOR:
    SELECT * FROM professor -- TODOS OS VALORES DO PROFESSOR
    SELECT * FROM professor where id = -- PESQUISA UM PROFESSOR ESPECÍFICO PELO ID(pk)

    -- TABELA DISCIPLINA:
    SELECT * FROM disciplina -- TODOS OS VALORES DA DISCIPLINA
    SELECT * FROM disciplina where id = -- PESQUISA UMA DISCIPLINA ESPECÍFICA PELO ID(pk)

    --TABELA CURSO
    SELECT * FROM curso -- TODOS OS VALORES DO CURSO
    SELECT * FROM curso where id = -- PESQUISA UM CURSO ESPECÍFICO PELO ID(pk)

    --TABELA ALUNO_TURMA_DISC
    SELECT * FROM aluno_turma_disc -- TODOS OS VALORES DO ALUNO_TURMA_DISC
    SELECT * FROM aluno_turma_disc where id = -- PESQUISA UM REGISTRO ALUNO_TURMA_DISC ESPECÍFICO PELO ID(pk)

    --TABELA TURMA
    select t.*, d.dia_segunda, d.dia_terca, d.dia_quarta, d.dia_quinta, d.dia_sexta from turma t, dias_semana_turma d where t.dias_semana = d.id -- TODOS OS VALORES DA TURMA ALÉM DOS DIAS DA SEMANA PARA FACILITAR A VISUALIZAÇÃO
    SELECT * FROM turma where id = -- PESQUISA UM REGISTRO DE TURMA ESPECÍFICA PELO ID(pk)

    --TABELA ENDERECO
    SELECT * FROM endereco -- TODOS OS VALORES DE ENDERECO
    SELECT * FROM endereco where id = -- PESQUISA UM ENDERECO ESPECÍFICO PELO ID(pk)

    --TABELA NOTAS
    SELECT * FROM notas -- TODOS OS VALORES DE NOTAS
    SELECT * FROM notas where id = -- PESQUISA UMA NOTA ESPECÍFICA PELO ID(pk)

    --TABELA CURSOS_ALUNOS
    SELECT * FROM cursos_alunos -- TODOS OS VALORES DE CURSOS_ALUNOS
    SELECT * FROM cursos_alunos where id =  -- PESQUISA UM REGISTRO DE CURSOS_ALUNOS PELO ID(pk)

    --TABELA CENTRO
    SELECT * FROM centro -- TODOS OS VALORES DE CENTRO
    SELECT * FROM centro where id = -- PESQUISA UM CENTRO PELO ID(pk)

    --TABELA CAMPUS
    SELECT * FROM campus  -- TODOS OS VALORES DE CAMPUS
    SELECT * FROM campus where id = -- PESQUISA UM CAMPUS PELO ID(pk)

    --TABELA REITOR
    SELECT * FROM reitor -- TODOS OS VALORES DE REITOR
    SELECT * FROM reitor where codigo = -- PESQUISA UM REITOR PELO CODIGO(pk)


    --TABELA LOCAL
    SELECT * FROM local -- TODOS OS VALORES DE LOCAL
    SELECT * FROM local where codigo = -- PESQUISA UM LOCAL PELO CODIGO(pk)

    --TABELA DIAS_SEMANA_TURMA
    SELECT * FROM dias_semana_turma
    SELECT * FROM dias_semana_turma where id = 

-- TRIGGERS E FUNCTIONS QUE IMPLEMENTAMOS NOS BANCOS

-- adicionar aluno
    CREATE OR REPLACE FUNCTION add_aluno() RETURNS TRIGGER 
    AS
    $BODY$
    BEGIN
        IF ((NEW.id_disc, NEW.id_turma) not in (select disciplina_id, id from turma)) 
        THEN RAISE EXCEPTION 'Turma Não Existe';
        ELSE
        UPDATE turma t
        SET qnt_alunos = (t.qnt_alunos + 1)
        FROM aluno_turma_disc a WHERE (t.id = NEW.id_turma);
        RETURN NEW;
        END IF;
    END;
    $BODY$
    LANGUAGE plpgsql;

    CREATE TRIGGER T_ADDALUNO
    AFTER INSERT ON aluno_turma_disc
    FOR EACH ROW
    EXECUTE PROCEDURE add_aluno();

    -- quando a turma eh atualizada
    CREATE OR REPLACE FUNCTION update_turma() RETURNS TRIGGER 
    AS
    $BODY$
    BEGIN
        IF NEW.vagas < NEW.qnt_alunos OR NEW.qnt_alunos < 0
        THEN RAISE EXCEPTION 'limite da turma atingido.';
        ELSE
            RETURN NEW;
        END IF;
    END;
    $BODY$
    LANGUAGE plpgsql;

    CREATE TRIGGER T_update_turma
    AFTER UPDATE ON turma
    FOR EACH ROW
    EXECUTE PROCEDURE update_turma();

    -- remover aluno
    CREATE OR REPLACE FUNCTION rem_aluno() RETURNS TRIGGER 
    AS
    $BODY$
    BEGIN
        UPDATE turma t
        SET qnt_alunos = qnt_alunos - 1 where t.id = OLD.id_turma;
        RETURN NEW;
    END;
    $BODY$
    LANGUAGE plpgsql;

    CREATE TRIGGER T_REMALUNO
    AFTER DELETE ON aluno_turma_disc
    FOR EACH ROW
    EXECUTE PROCEDURE rem_aluno();

    -- checar o cargo do professor
    CREATE OR REPLACE FUNCTION checa_cargo_professor() RETURNS TRIGGER
    AS
    $BODY$
    BEGIN
        IF (NEW.coord_curso_id IS NOT NULL) AND (NEW.diretor_centro_id IS NOT NULL)
        THEN RAISE EXCEPTION 'Professor não pode ser coordenador de um curso e diretor de um centro ao mesmo tempo.';
        ELSE RETURN NEW;
        END IF;
    END;
    $BODY$
    LANGUAGE plpgsql;

    CREATE TRIGGER T_CHECACARGOPROFESSOR
    AFTER INSERT OR UPDATE ON professor
    FOR EACH ROW
    EXECUTE PROCEDURE checa_cargo_professor();

    -- checar formatacao do semestre e horario alem da lotacao com numero de vagas
    CREATE OR REPLACE FUNCTION add_turma() RETURNS TRIGGER 
    AS
    $BODY$
    DECLARE
        numero_lotacao integer;
    BEGIN
        IF (NEW.semestre NOT LIKE '%.%') THEN RAISE EXCEPTION 'Erro, Semestre não está corretamente formatado';
        END IF;
        IF (NEW.horaini >= NEW.horafim) THEN RAISE EXCEPTION 'Horario final é antes do horario final';
        END IF;
        SELECT lotacao FROM local WHERE (codigo = NEW.local_id) INTO numero_lotacao;
        IF (NEW.vagas > numero_lotacao) THEN RAISE EXCEPTION 'O numero de vagas não pode exceder a lotação';
        END IF;
        RETURN NEW;
    END;
    $BODY$
    LANGUAGE plpgsql;

    CREATE TRIGGER T_ADDTURMA
    AFTER INSERT OR UPDATE ON turma
    FOR EACH ROW
    EXECUTE PROCEDURE add_turma();
    
    -- checar se local tem bloco nulo e
    -- chechar se a soma da lotacao das salas de um bloco eh menor que a lotacao total do bloco
    CREATE OR REPLACE FUNCTION add_local() RETURNS TRIGGER 
    AS
    $BODY$
    DECLARE 
        lotacao_total integer;
        lotacao_soma integer;
    BEGIN
        -- caso em que o local nao possui bloco
        IF upper(NEW.tipo) != 'B' AND (NEW.bloco IS NULL) THEN RAISE EXCEPTION 'Necessário Possuir um BLOCO';
        -- caso em que alteramos ou adicionamos um bloco
        ELSEIF upper(NEW.tipo) = 'B' THEN 
            SELECT SUM(lotacao) FROM local WHERE bloco = NEW.codigo INTO lotacao_soma;
            SELECT lotacao FROM local WHERE codigo = NEW.codigo INTO lotacao_total;
            IF lotacao_soma > lotacao_total
            THEN RAISE EXCEPTION 'Soma da lotação das salas ultrapassa a lotação total do bloco';
            END IF;
        -- caso em que adicionamos um local que o campo bloco nao esta nulo
        ELSEIF NEW.tipo != 'B' THEN 
            SELECT SUM(lotacao) FROM local WHERE bloco = NEW.bloco INTO lotacao_soma;
            SELECT lotacao FROM local WHERE codigo = NEW.bloco INTO lotacao_total;
            IF lotacao_soma > lotacao_total 
            THEN RAISE EXCEPTION 'Soma da lotação das salas ultrapassa a lotação total do bloco';
            END IF;
        END IF;
        
        RETURN NEW;
    END;
    $BODY$
    LANGUAGE plpgsql;

    CREATE TRIGGER T_ADDLOCAL
    AFTER INSERT OR UPDATE ON local
    FOR EACH ROW
    EXECUTE PROCEDURE add_local();

    -- checar quantidade de disciplinas que o professor leciona
    CREATE OR REPLACE FUNCTION add_disciplina() RETURNS TRIGGER 
    AS
    $BODY$
    DECLARE 
        numero integer;
    BEGIN
        Select count(professor_id) from disciplina where professor_id = NEW.professor_id into numero;
        IF (numero > 4) THEN RAISE EXCEPTION 'Um Professor não pode lecionar mais do que 4 disciplinas';
        ELSE
            RETURN NEW
        END IF;
    END;
    $BODY$
    LANGUAGE plpgsql;

    CREATE TRIGGER T_ADDDISCIPLINA
    AFTER INSERT OR UPDATE ON disciplina
    FOR EACH ROW
    EXECUTE PROCEDURE add_disciplina();

    --  turma existe e se um aluno não pode ser matriculado 2 vezes
    CREATE OR REPLACE FUNCTION add_atd() RETURNS TRIGGER 
    AS
    $BODY$
    BEGIN
        IF ((NEW.id_disc, NEW.id_turma) not in (select disciplina_id, id from turma))
        THEN RAISE EXCEPTION 'A TURMA NÃO É DA RESPECTIVA DISCIPLINA';
        ELSEIF((NEW.matr_aluno, NEW.id_disc) in (select matr_aluno, id_disc from aluno_turma_disc where id != NEW.id))
        THEN RAISE EXCEPTION 'UM MESMO ALUNO NÃO PODE SER MATRICULADO NA MESMA DISCIPLINA 2 VEZES';
        ELSE
        RETURN NEW;
        END IF;
    END;
    $BODY$
    LANGUAGE plpgsql;

    CREATE TRIGGER T_ADDATD
    AFTER INSERT OR UPDATE ON aluno_turma_disc
    FOR EACH ROW
    EXECUTE PROCEDURE add_atd();

    -- checar se aluno ta matriculado na disciplina q a nota ta sendo inserida
    CREATE OR REPLACE FUNCTION add_nota() RETURNS TRIGGER
    AS
    $BODY$
    BEGIN
        IF (NEW.id_disc NOT IN (SELECT id FROM disciplina))
        THEN RAISE EXCEPTION 'A DISCIPLINA NÃO EXISTE';
        ELSEIF (NEW.id_disc NOT IN (SELECT id_disc FROM aluno_turma_disc atd WHERE NEW.matr_aluno = atd.matr_aluno))
        THEN RAISE EXCEPTION 'O ALUNO NÃO ESTÁ MATRICULADO NA DISCIPLINA QUE A NOTA PERTENCE';
        ELSE RETURN NEW;
        END IF;
    END;
    $BODY$
    LANGUAGE plpgsql;

    CREATE TRIGGER T_ADDNOTA
    AFTER INSERT OR UPDATE ON notas
    FOR EACH ROW
    EXECUTE PROCEDURE add_nota()

    -- checar se o prof_id ja coordena um curso quando adicionar ou atualizar um curso (um professor so pode coordenar um curso)
    CREATE OR REPLACE FUNCTION add_curso() RETURNS TRIGGER
    AS
    $BODY$
    DECLARE
        coord_id integer;
    BEGIN
        SELECT coord_curso_id FROM professor p WHERE p.id = NEW.id_coord INTO coord_id;
        IF (coord_id IS NOT NULL and coord_id != old.id)
        THEN RAISE EXCEPTION 'Professor ja coordena um curso';
        END IF;
        
        UPDATE professor 
        SET coord_curso_id = NEW.id
        WHERE id = NEW.id_coord;
        
        RETURN NEW;
    END;
    $BODY$
    LANGUAGE plpgsql;

    CREATE TRIGGER T_ADDCURSO
    AFTER INSERT OR UPDATE ON curso
    FOR EACH ROW
    EXECUTE PROCEDURE add_curso();

    -- checar reitor nome e reitor data_nasc = prof nome prof data_nasc
    CREATE OR REPLACE FUNCTION add_reitor() RETURNS TRIGGER
    AS
    $BODY$
    BEGIN
        IF ((NEW.nome, NEW.data_nasc) NOT IN
        (SELECT nome, data_nasc FROM professor WHERE id = NEW.id_professor))
        THEN RAISE EXCEPTION 'Informações do reitor não correspondem ao do professor com o mesmo id';
        END IF;
        RETURN NEW;
    END;
    $BODY$
    LANGUAGE plpgsql;

    CREATE TRIGGER T_ADDREITOR
    AFTER INSERT OR UPDATE ON reitor
    FOR EACH ROW
    EXECUTE PROCEDURE add_reitor();

-- QUERYS ESPECÍFICAS REQUERIDAS
-- 1. Visualizar a média de cada aluno matriculado em uma turma já concluída.
-- checar no python se a turma entrada eh fechada (false)
SELECT aux.matr_aluno, aux.media
FROM
(SELECT atd.matr_aluno, atd.id_disc, atd.id_turma, AVG(n.valor) as media
FROM notas n, aluno_turma_disc atd, turma t
WHERE n.id_disc = atd.id_disc AND t.id = atd.id_turma AND atd.matr_aluno = n.matr_aluno AND t.estado = 'FECHADA'
GROUP BY (atd.matr_aluno, atd.id_disc, atd.id_turma)) aux
WHERE aux.id_turma = '3'; -- id_turma mutavel

-- 2. Verificar todas as turmas de determinado semestre.
SELECT * from turma
WHERE semestre = '1111.2'; -- semestre mutavel

-- 3. Quais locais estão em um dado bloco.
SELECT * FROM local WHERE bloco = '1'; -- bloco mutavel

-- 4. Visualizar quais turmas estão alocadas em determinado local, mostrando os nomes da turma 
-- e da disciplina e os horários de aula.
SELECT d.nome as disciplina_nome, t.id as turma_id, CONCAT(t.horaini, ' - ', t.horafim) as horario_aula
FROM turma t, local l, disciplina d
WHERE t.local_id = '1' -- local mutavel
AND d.id = t.disciplina_id AND t.local_id = l.codigo;

-- 5. Visualizar as médias de um aluno dada a matrícula. (Similar a um histórico escolar)
SELECT d.nome as disciplina, AVG(n.valor) as media
FROM notas n, disciplina d
WHERE d.id = n.id_disc AND matr_aluno = '509299' -- matricula mutavel
GROUP BY d.nome;

-- rascunho
SELECT * FROM notas;

DELETE FROM notas where id = 4;

insert into notas values(7,7.8,23,1);

SELECT matr_aluno, AVG(valor)
FROM notas 
GROUP BY matr_aluno;