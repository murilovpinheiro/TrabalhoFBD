from conectar import *
from tkinter import * 
from tkinter.ttk import * 

tabelas = getQuery('''
                   SELECT table_name 
                   FROM information_schema.tables
                   WHERE table_schema='public'
                   AND table_type='BASE TABLE';
                   ''')

root = Tk()
root.geometry("600x450")

botoes = []

for t in tabelas:
    botoes.append(Button(root, text= t[0]))
    botoes[len(botoes)-1].pack(side= 'top')

root.mainloop()