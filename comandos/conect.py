import psycopg2 as psc
from datetime import date

def conectar():
    conn = psc.connect(host = "######",
     database = "#####",
     user = "######",
     password = "######")
   # Colocar os valores respectivos do banco aqui
    
    return conn

def getQuery(com = "select * from aluno"):
    conn = conectar()
    cur = conn.cursor()
    cur.execute(com)
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado



# conn = conectar()
# cur = conn.cursor()

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

# cur.execute("select * from aluno")
# resultado = cur.fetchall()
# print(resultado)
# cur.close()
# conn.close()

# print(getQuery())
