# Bibliotecas
import tkinter as tk
from tkinter import ttk
from automato_finito_deterministico import Afd
from Textos import txts

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

        # Guia do Deterministico

        # Explicação da quintupla
        frm_afd = tk.LabelFrame(tab[0], text='O que é um Autômato Deterministico?', font=("Times new Roman", 15))
        tk.Label(frm_afd, text=txts['AFD'], justify='left', font=("Times new Roman", 15)).grid(column=0, row=0,
                                                                                               sticky='W')
        frm_afd.grid(column=0, row=0, columnspan=2, sticky='news', padx=(10, 10), pady=(10, 10))

        # Explicação da quintupla
        frm_5Tupla_explicacao = tk.LabelFrame(tab[0], text='Definição de uma 5-Tupla:', font=("Times new Roman", 15))
        tk.Label(frm_5Tupla_explicacao, text=txts['Exp5Tupla'], justify='left', font=("Times new Roman", 15)).grid(
            column=0, row=0, sticky='W')
        frm_5Tupla_explicacao.grid(column=0, row=1, sticky='news', padx=(10, 10), pady=(10, 10))

        # Coleta dados da quintupla
        self.edits_5Tupla = []  # 0-Conjunto de estados, 1-Alfabeto de entradas, 2-Estado inicial, 3-Estado final, 4-Regras
        frm_5Tupla_coleta = tk.LabelFrame(tab[0], text='Valores da sua 5-Tupla:', font=("Times new Roman", 15))
        for indc, txt in enumerate(txts['Col5Tupla']):
            self.edits_5Tupla.append(tk.Entry(frm_5Tupla_coleta, bd=2, width=50))
            tk.Label(frm_5Tupla_coleta, text=txt, justify='left', font=("Times new Roman", 15)).grid(column=0, row=indc, sticky='W')
            self.edits_5Tupla[indc].grid(column=1, row=indc, sticky='W', padx=(5, 5))
        frm_5Tupla_coleta.grid(column=0, row=2, sticky='news', padx=(10, 10), pady=(10, 10))

        # Botao inicia
        btn_start = tk.Button(frm_5Tupla_coleta, text="Iniciar", width=10, height=3, command=self.inicia_prog)
        btn_start.grid(column=1, row=5, sticky='ne', padx=(5, 5))
        btn_start = tk.Button(frm_5Tupla_coleta, text="teste", width=10, height=3, command=self.teste_insert)
        btn_start.grid(column=0, row=5, sticky='ne', padx=(5, 5))

        # Coleta regra de transicao
        frm_regras_trans = tk.LabelFrame(tab[0], text='Regras de Transição da sua 5-Tupla:', font=("Times new Roman", 15))
        self.edits_5Tupla.append(tk.Text(frm_regras_trans, bd=2, width=50))
        scrl_5Tupla = tk.Scrollbar(frm_regras_trans)
        self.edits_5Tupla[5].configure(yscrollcommand=scrl_5Tupla.set)
        scrl_5Tupla.config(command=self.edits_5Tupla[5].yview)
        self.edits_5Tupla[5].pack(side=tk.LEFT)
        scrl_5Tupla.pack(side=tk.RIGHT, fill=tk.Y)
        frm_regras_trans.grid(column=1, row=1, rowspan=2, padx=(10, 10), pady=(10, 10))

        # Inicializacao
        janela.mainloop()

    def teste_insert(self):
        self.edits_5Tupla[0].insert(0, 'q0, q1, q2, qf')
        self.edits_5Tupla[1].insert(0, '0, 1')
        self.edits_5Tupla[2].insert(0, 'q0')
        self.edits_5Tupla[3].insert(0, 'qf')
        self.edits_5Tupla[4].insert(0, '01110')
        self.edits_5Tupla[5].insert('1.0', 'q0, 0, q1\nq1, 1, q2\nq2, 1, q1\nq2, 0, qf\n')

    def inicia_prog(self):
        self.dados = {
            'Q': self.edits_5Tupla[0].get().replace(',', '').split(),
            'E': self.edits_5Tupla[1].get().replace(',', '').split(),
            'q': self.edits_5Tupla[2].get().replace(',', '').split(),
            'F': self.edits_5Tupla[3].get().replace(',', '').split(),
            'P': self.edits_5Tupla[4].get(),
            'FT': [elem.replace(',', '').split() for elem in self.edits_5Tupla[5].get('1.0', tk.END).split('\n') if elem != '']
        }

        auto = Afd()
        auto.set_5upla(self.dados)
        auto.mostrar_dados()
        validacao_automato = auto.validar_automato()
        if validacao_automato:
            validacao_palavra = auto.ler_palavra()
            if validacao_palavra:
                print("\n # Palavra valida!")
            else:
                print("\n # Palavra invalida!")

