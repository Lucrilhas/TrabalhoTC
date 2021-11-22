import tkinter as tk
from tkinter import ttk
from Textos import txts
from automato_finito_deterministico import Afd
from ScrollFrame import ScrollableFrame
from grafos import DesenhaAutomato
from PIL import ImageTk, Image

class Tab_AFD():
    def __init__(self, janela):
        # Canvas Principal
        fs = ScrollableFrame(janela)
        fs.pack(fill='both', expand=True)
        fsp = fs.scrollable_frame

        # Explicação da AFD
        frm_afd = tk.LabelFrame(fsp, text='O que é um Autômato Deterministico?', font=("Times new Roman", 15))
        tk.Label(frm_afd, text=txts['AFD'], justify='left', font=("Times new Roman", 15)).grid(column=0, row=0,
                                                                                               sticky='W')
        frm_afd.grid(column=0, row=0, columnspan=2, sticky='news', padx=(10, 10), pady=(10, 10))

        # Explicação da quintupla
        frm_5Tupla_explicacao = tk.LabelFrame(fsp, text='Definição de uma 5-Tupla:', font=("Times new Roman", 15))
        tk.Label(frm_5Tupla_explicacao, text=txts['Exp5Tupla'], justify='left', font=("Times new Roman", 15)).grid(
            column=0, row=0, sticky='W')
        frm_5Tupla_explicacao.grid(column=0, row=1, sticky='news', padx=(10, 10), pady=(10, 10))

        # Coleta dados da quintupla
        self.edits_5Tupla = []  # 0-Conjunto de estados, 1-Alfabeto de entradas, 2-Estado inicial, 3-Estado final, 4-Regras
        frm_5Tupla_coleta = tk.LabelFrame(fsp, text='Valores da sua 5-Tupla:', font=("Times new Roman", 15))
        for indc, txt in enumerate(txts['Col5Tupla']):
            self.edits_5Tupla.append(tk.Entry(frm_5Tupla_coleta, bd=2, width=50))
            tk.Label(frm_5Tupla_coleta, text=txt, justify='left', font=("Times new Roman", 15)).grid(column=0, row=indc,
                                                                                                     sticky='W')
            self.edits_5Tupla[indc].grid(column=1, row=indc, sticky='W', padx=(5, 5))
        frm_5Tupla_coleta.grid(column=0, row=2, sticky='news', padx=(10, 10), pady=(10, 10))

        # Botao inicia
        btn_start = tk.Button(frm_5Tupla_coleta, text="Iniciar", width=10, height=3, command=self.inicia_prog)
        btn_start.grid(column=1, row=5, sticky='ne', padx=(5, 5))
        btn_start = tk.Button(frm_5Tupla_coleta, text="teste", width=10, height=3, command=self.teste_insert)
        btn_start.grid(column=0, row=5, sticky='ne', padx=(5, 5))

        # Coleta regra de transicao
        frm_regras_trans = tk.LabelFrame(fsp, text='Regras de Transição da sua 5-Tupla:',
                                         font=("Times new Roman", 15))
        self.edits_5Tupla.append(tk.Text(frm_regras_trans, bd=2, width=50))
        scrl_5Tupla = tk.Scrollbar(frm_regras_trans)
        self.edits_5Tupla[5].configure(yscrollcommand=scrl_5Tupla.set)
        scrl_5Tupla.config(command=self.edits_5Tupla[5].yview)
        self.edits_5Tupla[5].pack(side=tk.LEFT)
        scrl_5Tupla.pack(side=tk.RIGHT, fill=tk.Y)
        frm_regras_trans.grid(column=1, row=1, rowspan=2, padx=(10, 10), pady=(10, 10))

        # Erro de entradas
        self.frm_erro = tk.LabelFrame(fsp, text='Erro!:', font=("Times new Roman", 15))
        self.lbl_erro = tk.Label(self.frm_erro, text='Erro tal', justify='left', font=("Times new Roman", 15))

        # Resultados
        self.frm_resul = tk.LabelFrame(fsp, text='Resultado:', font=("Times new Roman", 15))
        self.lbl_resul = tk.Label(self.frm_resul, text='resultado tal', justify='left', font=("Times new Roman", 15))

        # Imagem Resultado
        self.frm_img = tk.LabelFrame(fsp, text='Representação Visual:', font=("Times new Roman", 15))
        self.lbl_img = None



    def teste_insert(self):
        # self.edits_5Tupla[0].insert(0, 'q0, q1, q2, qf')
        # self.edits_5Tupla[1].insert(0, '0, 1')
        # self.edits_5Tupla[2].insert(0, 'q0')
        # self.edits_5Tupla[3].insert(0, 'qf')
        # self.edits_5Tupla[4].insert(0, '01110')
        # self.edits_5Tupla[5].insert('1.0', 'q0, 0, q1\nq1, 1, q2\nq2, 1, q1\nq2, 0, qf\n')
        self.edits_5Tupla[0].insert(0, 's0, s1, s2, s3, s4')
        self.edits_5Tupla[1].insert(0, 'a, b')
        self.edits_5Tupla[2].insert(0, 's0')
        self.edits_5Tupla[3].insert(0, 's4')
        self.edits_5Tupla[4].insert(0, 'ababa')
        self.edits_5Tupla[5].insert('1.0', 's0, a, s1\ns0, b, s2\ns1, a, s1\ns1, b, s3\ns2, a, s1\ns2, b, s2\ns3, a, s1\ns3, b, s4\ns4, a, s1\ns4, b, s2')

    def inicia_prog(self):
        self.dados = {
            'Q': self.edits_5Tupla[0].get().replace(',', '').split(),
            'E': self.edits_5Tupla[1].get().replace(',', '').split(),
            'q': self.edits_5Tupla[2].get().replace(',', '').split(),
            'F': self.edits_5Tupla[3].get().replace(',', '').split(),
            'P': self.edits_5Tupla[4].get(),
            'FT': [elem.replace(',', '').split() for elem in self.edits_5Tupla[5].get('1.0', tk.END).split('\n') if
                   elem != '']
        }

        for k in self.dados:
            print(k, self.dados[k])

        auto = Afd()
        auto.set_5upla(self.dados)
        validacao_automato = auto.validar_automato()
        print(validacao_automato)
        if validacao_automato == 'Ok':
            self.frm_erro.grid_forget()
            self.lbl_resul['text'] = auto.ler_palavra()
            self.lbl_resul.pack()
            self.frm_resul.grid(column=0, row=4, columnspan=2, sticky='news', padx=(10, 10), pady=(10, 10))
            n_img = 'imgs/imagem_auto.png'
            dg = DesenhaAutomato(self.dados)
            dg.plota(n_img)

            self.coloca_img(n_img)

        else:
            self.lbl_erro['text'] = validacao_automato
            self.lbl_erro.pack()
            self.frm_erro.grid(column=0, row=3, columnspan=2, sticky='news', padx=(10, 10), pady=(10, 10))

    def coloca_img(self, n_img):
        img = Image.open(n_img)
        test = ImageTk.PhotoImage(img)
        # if self.lbl_img is not None:
        #     self.lbl_img.pack_forget()
        self.frm_img.grid(column=0, row=5, columnspan=2, sticky='news', padx=(10, 10), pady=(10, 10))
        self.lbl_img = tk.Label(self.frm_img, image=test)
        self.lbl_img.image = test
        self.lbl_img.pack()


