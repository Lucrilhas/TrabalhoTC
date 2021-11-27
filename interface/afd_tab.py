import tkinter as tk
from tkinter import ttk, messagebox
from Textos import txts
from automatos.automato_finito_deterministico import Afd
from interface.ScrollFrame import ScrollableFrame
from PIL import ImageTk, Image
from interface.backend import *


TIMES15 = ("Times new Roman", 15)


class AFD_Tab:
    def __init__(self, janela):
        sf = ScrollableFrame(janela)
        sf.pack(fill='both', expand=True)
        fsf = sf.scrollable_frame

        # Variaveis do tkinter
        vars = {
            'cbbox': tk.StringVar()
        }
        # Filhos da janela principal
        self.pais = {
            'afd_exp':  tk.LabelFrame(fsf, text='O que é um Autômato Deterministico?', font=TIMES15),
            '5t_exp':   tk.LabelFrame(fsf, text='Definição de uma 5-Tupla:', font=TIMES15),
            '5t_vals':  tk.LabelFrame(fsf, text='Valores da sua 5-Tupla:', font=TIMES15),
            '5t_fts':   tk.LabelFrame(fsf, text='Regras de Transição da sua 5-Tupla:', font=TIMES15),
            'acoes':    tk.LabelFrame(fsf, text='Ações:', font=TIMES15),
            'result':   tk.LabelFrame(fsf, text='Resultado:', font=TIMES15),
            'imgs':     tk.LabelFrame(fsf, text='Representação Visual:', font=TIMES15)
        }

        # Filhos dos Labelframe (Pais)
        self.filhos = {
            'exp_afd':  tk.Label(self.pais['afd_exp'], text=txts['AFD'], justify='left', font=TIMES15),
            'exp_5t':   tk.Label(self.pais['5t_exp'], text=txts['EXP_5T'], justify='left', font=TIMES15),
            '5t_vals':  [tk.Label(self.pais['5t_vals'], text=txt, justify='left', font=TIMES15) for txt in txts['VAL_5T']],
            'edts':     [tk.Entry(self.pais['5t_vals'], bd=2, width=50) for _ in txts['VAL_5T']],
            'ft_scrl':  tk.Scrollbar(self.pais['5t_fts']),
            'ft':       tk.Text(self.pais['5t_fts'], bd=2, width=50, height=20),
            'btn_ini':  tk.Button(self.pais['acoes'], text="Iniciar", width=10, height=2, command=self.iniciar),
            'btn_list': tk.Button(self.pais['acoes'], text="Salvar Atual", width=10, height=2, command=self.salvar),
            'btn_save': tk.Button(self.pais['acoes'], text="Usar Salvo", width=10, height=2, command=self.insere_salvo),
            'cbbox':     ttk.Combobox(self.pais['acoes'], textvariable=vars['cbbox'])

        }

        self.config_iniciais()
        self.coloca_iniciais()

    def config_iniciais(self):
        self.filhos['ft'].configure(yscrollcommand=self.filhos['ft_scrl'].set)  # Config Scroll memo
        self.filhos['ft_scrl'].config(command=self.filhos['ft'].yview)  # Config Scroll memo

        self.filhos['cbbox']['values'] = [n['name'].replace('.txt', '') for n in get_afd_tests()]   # Lista de salvos

    # Coloca os widgets iniciais
    def coloca_iniciais(self):
        # Pais
        self.pais['afd_exp'].grid(column=0, row=0, columnspan=2, sticky='news', padx=(10, 10), pady=(10, 10))
        self.pais['5t_exp'].grid(column=0, row=1, sticky='news', padx=(10, 10), pady=(10, 10))
        self.pais['5t_vals'].grid(column=0, row=2, sticky='news', padx=(10, 10), pady=(10, 10))
        self.pais['5t_fts'].grid(column=1, row=1, rowspan=2, sticky='news', padx=(10, 10), pady=(10, 10))
        self.pais['acoes'].grid(column=0, row=3, columnspan=2, sticky='news', padx=(10, 10), pady=(10, 10))

        self.filhos['exp_afd'].grid(column=0, row=0, sticky='nw')   # Filho da label de explicação do AFD
        self.filhos['exp_5t'].grid(column=0, row=0, sticky='nw')    # Filho da label de explicação da 5-Tupla


        self.filhos['ft'].pack(side=tk.LEFT)    # Memo das Funções de transição
        self.filhos['ft_scrl'].pack(side=tk.RIGHT, fill=tk.Y)   # Scroll Memo

        for n, _ in enumerate(txts['VAL_5T']):
            self.filhos['5t_vals'][n].grid(column=0, row=n, sticky='nw')    # Labels valores
            self.filhos['edts'][n].grid(column=1, row=n, sticky='nw')       # Edits valores

        self.filhos['btn_ini'].grid(column=2, row=0)    # Botao de iniar processamento
        self.filhos['btn_list'].grid(column=0, row=0)   # Botao de import arquivo
        self.filhos['btn_save'].grid(column=1, row=0)   # Botao de export arquivo
        self.filhos['cbbox'].grid(column=0, row=1)      # Combobox de select arquivo


    # Inicia o processamento do automato
    def iniciar(self):
        valores = self.get_valores(True)
        auto_afd = Afd()
        auto_afd.set_5upla(valores)
        #auto_afd.mostrar_dados()
        valid = auto_afd.validar_automato()

        if valid == 'Ok':
            a = auto_afd.ler_palavra()
            print(a)
        else:
            messagebox.showerror("Palavra Inválida!", valid)

    # Salva em um arquivo os valores da interface
    def salvar(self):
        if self.filhos['cbbox'].current() == -1:
            salvar_afd(self.get_valores(False), self.filhos['cbbox'].get())
        elif messagebox.askokcancel('Certeza?', 'Você tem certeza que quer reescrever esse arquivo?'):
            salvar_afd(self.get_valores(False), self.filhos['cbbox'].get())

    def get_valores(self, puro):
        if puro:
            valores = {
                'q': self.filhos['edts'][0].get().replace(',', '').split(),
                'e': self.filhos['edts'][1].get().replace(',', '').split(),
                'i': self.filhos['edts'][2].get().replace(',', '').split(),
                'f': self.filhos['edts'][3].get().replace(',', '').split(),
                'p': self.filhos['edts'][4].get().replace(',', '').split(),
                'ft': [elem.replace(',', '').split() for elem in self.filhos['ft'].get('1.0', tk.END).split('\n') if elem != '']
            }
        else:
            valores = {
                'q': self.filhos['edts'][0].get(),
                'e': self.filhos['edts'][1].get(),
                'i': self.filhos['edts'][2].get(),
                'f': self.filhos['edts'][3].get(),
                'p': self.filhos['edts'][4].get(),
                'ft': self.filhos['ft'].get('1.0', tk.END)
            }
        return valores

    # Pega o arquivo salva e insere seus valores na interface
    def insere_salvo(self):
        if self.filhos['cbbox'].current() != -1:
            file = get_afd_tests()[self.filhos['cbbox'].current()]
            self.filhos['edts'][0].insert(0, file['q'])
            self.filhos['edts'][1].insert(0, file['e'])
            self.filhos['edts'][2].insert(0, file['i'])
            self.filhos['edts'][3].insert(0, file['f'])
            # self.filhos['edts'][4].insert(0, file['ft']) # Palavra
            for ft in file['ft']:
                self.filhos['ft'].insert(tk.END, ft)

        else:
            messagebox.showerror("Erro!", "Selecione um item válido!")