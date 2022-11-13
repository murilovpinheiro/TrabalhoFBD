CREATE OR REPLACE FUNCTION add_aluno() RETURNS TRIGGER 
AS
$BODY$
BEGIN
	UPDATE turma t
	SET qnt_alunos = (t.qnt_alunos + 1)
	FROM aluno_turma_disc a WHERE (t.id = NEW.id_turma);
	RETURN NEW;
END;
$BODY$
LANGUAGE plpgsql;

CREATE TRIGGER T_ADDALUNO
AFTER INSERT ON aluno_turma_disc
FOR EACH ROW
EXECUTE PROCEDURE add_aluno();

CREATE OR REPLACE FUNCTION update_turma() RETURNS TRIGGER 
AS
$BODY$
BEGIN
    IF NEW.vagas < NEW.qnt_alunos
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