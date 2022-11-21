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