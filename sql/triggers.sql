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

-- checar formatacao do semestre e horario alem da lotacao
CREATE OR REPLACE FUNCTION add_turma() RETURNS TRIGGER 
AS
$BODY$
DECLARE
    numero_lotacao integer;
BEGIN
    IF (NEW.semestre NOT LIKE '{%.%}') THEN RAISE EXCEPTION 'Erro, Semestre não está corretamente formatado';
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
 
-- checar bloco
CREATE OR REPLACE FUNCTION add_local() RETURNS TRIGGER 
AS
$BODY$
BEGIN
        IF upper(NEW.tipo) != 'B' AND (NEW.bloco IS NULL) THEN RAISE EXCEPTION 'Necessário Possuir um BLOCO';
        ELSE
            RETURN NEW;
        END IF;
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