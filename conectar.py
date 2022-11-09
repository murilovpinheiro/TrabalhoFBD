import psycopg2 as psc
from datetime import date

def conectar():
    conn = psc.connect(host = "200.129.44.249",
     database = "510613",
     user = "510613",
     password = "510613@fbd")
    return conn

conn = conectar()
cur = conn.cursor()
# try:
#     cur.execute("INSERT INTO aluno(nome, sexo, data_nasc, endereco) values (%s, %s, %s, %s);", ("Papai Noel", "F", "2004-2-2", "ab"))
#     conn.commit()
# except Exception as e:
#     if (str(e).find("invalid input syntax for type integer") )> -1:
#         print("Valor Digitado Inválido")
#     #é assim que irei tratar os erros mais comuns
#     #Erros comuns vão ser computados apenas como erros ao inicio, se sobrar tempo eu faço tratamento melhor
# except Exception as e:
#     print(e)
cur.execute("select * from aluno")
resultado = cur.fetchall()
print(resultado)
cur.close()
conn.close()