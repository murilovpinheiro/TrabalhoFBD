ALTER TABLE turma add check (estado IN ('ABERTA', 'FECHADA'));

ALTER TABLE aluno add check (sexo IN ('o', 'f', 'm', 'O', 'F', 'M'));

ALTER TABLE turma add check (dia_segunda IN ('SIM', 'NÃO'));

ALTER TABLE turma add check (dia_terca IN ('SIM', 'NÃO'));

ALTER TABLE turma add check (dia_quarta IN ('SIM', 'NÃO'));

ALTER TABLE turma add check (dia_quinta IN ('SIM', 'NÃO'));

ALTER TABLE turma add check (dia_sexta IN ('SIM', 'NÃO'));