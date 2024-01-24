import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title('Meu relógio')
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background='#4b0082')

#Funções

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text = 'Olá, ' + nome_usuario)

def get_data():
    data_atual = strftime('%a, %d %b %Y')
    data.config(text = data_atual)

def get_hora():
    hora_atual = strftime('%H:%M:%S')
    hora.config(text = hora_atual)
    hora.after(1000, get_hora)

tela = tk.Canvas(root, width=600, height=60, bg='#4b0082', bd=0, highlightthickness=0, relief='ridge')
tela.pack()

saudacao = Label(root, bg='#4b0082', fg='#fff', font=('sans-serif', 16))
saudacao.pack()

data = Label(root, bg='#4b0082', fg='#fff', font=('sans-serif', 14))
data.pack(pady=2)

hora = Label(root, bg='#4b0082', fg='#fff', font=('sans-serif', 64))
hora.pack(pady=2)

get_saudacao()
get_data()
get_hora()
root.mainloop()


