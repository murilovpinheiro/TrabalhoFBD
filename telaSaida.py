from tkinter import *
import psycopg2 as psc

def conectar():
    conn = psc.connect(host = "200.129.44.249",
     database = "510613",
     user = "510613",
     password = "510613@fbd")
    return conn

def consultar():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("select * from aluno")
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado

def criarFrame():
    frame = Frame()
    result = consultar()
    for i in range(len(result)):
        for j in range(6):
            e = Label(frame,font=('Helvetica',12), background = "#e6e6ff" , width = 10,text = str(result[i][j]), borderwidth = 1, relief = "solid", anchor = "e")
            e.grid(row = i, column = j)
            print(result[i][j])
    return frame