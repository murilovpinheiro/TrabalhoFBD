from tkinter import *
from  tkinter import ttk
from tkinter.messagebox import showinfo
import psycopg2 as psc

def conectar():
    conn = psc.connect(host = "200.129.44.249",
                       database = "510613",
                       user = "510613",
                       password = "510613@fbd")
    return conn

def pesquisar(codigo, valor):
    conn = conectar()
    cursor = conn.cursor()
    string = codigo + "'"+ valor +"'"
    cursor.execute(string)
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    names = ('Nome: ', 'Sexo: ', 'Data de Nascimento: ',
         'Endereço: ', 'Email: ')
    createForm(names, frame, {}, resultado)


def createSearch(nome, codigo, local):
    lb = ttk.Label(local, text = nome)
    e = ttk.Entry(local)
    lb.pack( expand = True, pady = 10, side = TOP, anchor = CENTER)
    e.pack( expand = True, side = TOP, anchor = CENTER, ipadx = 50)
    button = ttk.Button(frame, text = "Pesquisar", command = lambda: pesquisar(codigo, e.get()))
    button.pack( expand = True, pady = 25, anchor = CENTER)

def createForm(names, local, entrys, resultado):
    i = 1
    for name in names:
        lb = ttk.Label(local, text = name)
        e = ttk.Entry(local)
        entrys[name] = e
        lb.pack( expand = True, pady = 10, side = TOP, anchor = CENTER)
        e.pack( expand = True, side = TOP, anchor = CENTER, ipadx = 50)
        if resultado[0][i] != None:
            e.insert(END, resultado[0][i])
        i+=1
    button = ttk.Button(frame, text = "Pesquisar", command = inserir)
    button.pack( expand = True, pady = 25, anchor = CENTER)

def inserir():
    string = ''
    for i in range(len(names)):
        string = string + "'" + entrys[names[i]].get() + "'"
        if i == len(names) - 1:
            break
        string = string + ","
    string = "INSERT INTO aluno(nome, sexo, data_nasc, endereco, email) values (" + string + ");"
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute(string)
        conn.commit()
        showinfo("Aviso: ", "Salvou")
    except Exception as e:
        showinfo("ERRO",("Dados Digitados são Inválidos: \n %e", e))
        if (str(e).find("invalid input syntax for type integer") )> -1:
            print("Valor Digitado Inválido")
    cursor.close()
    conn.close()

root = Tk()
root.title("Tela Dinamica")
root.geometry("600x450")
root.resizable(False, False)



frame = ttk.Frame(root)
frame.pack(padx = 10, pady = 0, fill = "x", expand = True)
nome = "Pesquise um aluno pela Matrícula: "
createSearch(nome, "select * from aluno where matricula = ", frame)

root.mainloop()