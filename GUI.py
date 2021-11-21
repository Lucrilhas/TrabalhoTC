# Bibliotecas
import tkinter as tk
from tkinter import ttk
import Automato as aut
from Textos import txts

# Constantes
TAMANHO_PROG = (1000, 800)
AZUL_CLARO = '#ADD8E6'

# Classe de inteface
class Programa:
    def __init__(self):
        # Variaveis de configuração

        # Variaveis de interface
        janela = tk.Tk()  # Janela mais profunda
        janela.title('Automatos de Pilha')         # Nome da janela
        janela.geometry(f'{TAMANHO_PROG[0]}x{TAMANHO_PROG[1]}')   # Tamanho da janela
        janela.iconbitmap('imgs/icone_janela.ico')    # Icone
        janela['bg'] = AZUL_CLARO

        # Divide a janela em header e Body
        header = tk.Frame(janela, height=100)
        header.pack(fill='x', side='top')
        div = tk.Frame(janela, bg='black', height=5)    # Linha de divisão entre
        div.pack(fill='x', side='top')
        body = tk.Frame(janela, bg=AZUL_CLARO)
        body.pack(fill='both', expand=True, side='top')

        # Dentro Header
        tk.Label(header, text='Trabalho de Teoria da Computação - Automatos Finitos', font=("Arial Bold", 25)).pack()

        # Guias do Body
        tabs = ttk.Notebook(body)
        tabs.pack(fill='both', expand=True)

        tab = [ttk.Frame(tabs) for _ in enumerate(txts['Guias'])]

        for t, txt in zip(tab, txts['Guias']):
            t.pack(fill='both', expand=True)
            tabs.add(t, text=txt)

        # Guia do Deterministico

        # Explicação da quintupla
        frm_5Tupla_explicacao = tk.LabelFrame(tab[0], text='Definição de uma 5-Tupla:', font=("Times new Roman", 15))
        tk.Label(frm_5Tupla_explicacao, text= txts['Exp5Tupla'], justify='left', font=("Times new Roman", 15)).grid(column=0, row=0, sticky='W')
        frm_5Tupla_explicacao.grid(column=0, row=0, sticky='W', padx=(10,10), pady=(10,10))

        # Coleta dados da quintupla
        edits_5Tupla = []
        frm_5Tupla_coleta = tk.LabelFrame(tab[0], text='Valores da sua 5-Tupla:', font=("Times new Roman", 15))
        for indc, txt in enumerate(txts['Col5Tupla']):
            edits_5Tupla.append(tk.Entry(frm_5Tupla_coleta, bd=2, width=50))
            tk.Label(frm_5Tupla_coleta, text=txt, justify='left', font=("Times new Roman", 15)).grid( column=0, row=indc, sticky='W')
            edits_5Tupla[indc].grid( column=1, row=indc, sticky='W', padx=(5, 5))
        frm_5Tupla_coleta.grid(column=1, row=0, sticky='W', padx=(10, 10), pady=(10, 10))


        # Inicializacao
        janela.mainloop()