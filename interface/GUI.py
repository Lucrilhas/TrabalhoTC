# Bibliotecas
import tkinter as tk
from tkinter import ttk
from Textos import txts
from interface.afd_tab import AFD_Tab
# from bk.tab_AFD import Tab_AFD

# Constantes
TAMANHO_PROG = (1000, 800)
AZUL_CLARO = '#ADD8E6'


# Classe de inteface
class Programa:
    def __init__(self):
        # Variaveis de configuração
        self.dados = None
        # Variaveis de interface
        janela = tk.Tk()  # Janela mais profunda
        janela.title('Automatos de Pilha')  # Nome da janela
        janela.geometry(f'{TAMANHO_PROG[0]}x{TAMANHO_PROG[1]}')  # Tamanho da janela
        janela.iconbitmap('imgs/icone_janela.ico')  # Icone
        janela['bg'] = AZUL_CLARO

        # Divide a janela em header e Body
        header = tk.Frame(janela, height=100)
        header.pack(fill='x', side='top')
        div = tk.Frame(janela, bg='black', height=5)  # Linha de divisão entre
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

        ### Guia do Deterministico
        AFD_Tab(tab[0])
        # Tab_AFD(tab[1])

        # Inicializacao
        janela.mainloop()