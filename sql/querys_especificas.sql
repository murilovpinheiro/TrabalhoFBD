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