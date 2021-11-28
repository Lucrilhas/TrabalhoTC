import tkinter as tk
from tkinter import ttk, messagebox
from Textos import txts
from interface.ScrollFrame import ScrollableFrame
from interface.backend import *

TIMES15 = ("Times new Roman", 15)

class Front:
    def __init__(self, janela, infos):
        self.infos = infos

        # Variavei comuns
        self.passo_atual = 0    # Indice de imagem/label atual
        self.passos = None      # Dicionario que guarda informacoes de cada passo/etapa
        self.imgs = []          # Array de imagens a der mostradas
        self.resultado = None   # Resultado recebido do backend

        # Fundo da Janela com scroll
        sf = ScrollableFrame(janela)
        sf.pack(fill='both', expand=True)
        fsf = sf.scrollable_frame

        # Variaveis do tkinter
        tk_vars = {
            'cbbox': tk.StringVar()     # Guarda o texto do Combobox
        }

        # Primeiro nível de widgets - Filhos da janela principal
        self.pais = {
            'exp_auto':  tk.LabelFrame(fsf, text=infos['auto_exp'], font=TIMES15),                      # Explicação do automato
            '5t_exp':   tk.LabelFrame(fsf, text='Definição de uma 5-Tupla:', font=TIMES15),             # Explicação da 5-Tupla
            '5t_vals':  tk.LabelFrame(fsf, text='Valores da sua 5-Tupla:', font=TIMES15),               # Coleta a 5-Tupla
            '5t_fts':   tk.LabelFrame(fsf, text='Regras de Transição da sua 5-Tupla:', font=TIMES15),   # Coleta as regras de transicao
            'acoes':    tk.LabelFrame(fsf, text='Ações:', font=TIMES15),            # Ações para o usuario
            'result':   tk.LabelFrame(fsf, text='Resultado:', font=TIMES15),        # Resultado final
            'leg':      tk.LabelFrame(fsf, text='Legenda Gráfico:', font=TIMES15),  # Legenda do grafico
        }

        # Segundo nível de widgets - Filhos dos pais
        self.filhos = {
            'exp_auto': tk.Label(self.pais['exp_auto'], text=txts[infos['indc_txt']], justify='left', font=TIMES15),
            'exp_5t':   tk.Label(self.pais['5t_exp'], text=txts['EXP_5T'], justify='left', font=TIMES15),
            '5t_vals': [tk.Label(self.pais['5t_vals'], text=txt, justify='left', font=TIMES15) for txt in txts['VAL_5T']],
            'edts':    [tk.Entry(self.pais['5t_vals'], bd=2, width=50) for _ in txts['VAL_5T']],
            'ft_scrl':  tk.Scrollbar(self.pais['5t_fts']),
            'ft':       tk.Text(self.pais['5t_fts'], bd=2, width=50, height=20),
            'btn_ini':  tk.Button(self.pais['acoes'], text="Iniciar", width=10, height=2, command=self.iniciar),
            'btn_list': tk.Button(self.pais['acoes'], text="Salvar Atual", width=10, height=2, command=self.salvar),
            'btn_save': tk.Button(self.pais['acoes'], text="Usar Salvo", width=10, height=2, command=self.insere_salvo),
            'btn_del':  tk.Button(self.pais['acoes'], text="Limpar textos", width=10, height=2, command=self.limpar),
            'cbbox':    ttk.Combobox(self.pais['acoes'], textvariable=tk_vars['cbbox'], width=25),
            'btn_dir':  tk.Button(self.pais['result'], text=">>", width=10, height=2, command=self.go_direita),
            'btn_esq':  tk.Button(self.pais['result'], text="<<", width=10, height=2, command=self.go_esquerda),
            'exp_img':  tk.Label(self.pais['result'], justify='left', font=TIMES15),
            'img':      tk.Label(self.pais['result']),
            'leg':      tk.Label(self.pais['leg'], text=txts['LEG'], justify='left', font=TIMES15),
        }

        # Configurações iniciais
        self.filhos['ft'].configure(yscrollcommand=self.filhos['ft_scrl'].set)  # Config Scroll memo
        self.filhos['ft_scrl'].config(command=self.filhos['ft'].yview)  # Config Scroll memo

        self.filhos['cbbox']['values'] = [n['name'].replace('.txt', '') for n in get_tests(infos['path_tests'])]  # Lista de salvos
        self.pais['acoes'].grid_columnconfigure(3, weight=1)    # Pos btn limpar pro lado

        # Colocar widgets iniciais
        # Pais
        self.pais['exp_auto'].grid(column=0, row=0, columnspan=2, sticky='news', padx=(10, 10), pady=(10, 10))
        self.pais['5t_exp'].grid(column=0, row=1, sticky='news', padx=(10, 10), pady=(10, 10))
        self.pais['5t_vals'].grid(column=0, row=2, sticky='news', padx=(10, 10), pady=(10, 10))
        self.pais['5t_fts'].grid(column=1, row=1, rowspan=2, sticky='news', padx=(10, 10), pady=(10, 10))
        self.pais['acoes'].grid(column=0, row=3, columnspan=2, sticky='news', padx=(10, 10), pady=(10, 10))

        # Filhos
        self.filhos['exp_auto'].grid(column=0, row=0, sticky='nw')  # Filho da label de explicação do auto
        self.filhos['exp_5t'].grid(column=0, row=0, sticky='nw')  # Filho da label de explicação da 5-Tupla

        self.filhos['ft'].pack(side=tk.LEFT)  # Memo das Funções de transição
        self.filhos['ft_scrl'].pack(side=tk.RIGHT, fill=tk.Y)  # Scroll Memo

        for n, _ in enumerate(txts['VAL_5T']):
            self.filhos['5t_vals'][n].grid(column=0, row=n, sticky='nw')  # Labels valores
            self.filhos['edts'][n].grid(column=1, row=n, sticky='nw')  # Edits valores

        self.filhos['btn_ini'].grid(column=2, row=0)  # Botao de iniar processamento
        self.filhos['btn_list'].grid(column=0, row=0)  # Botao de import arquivo
        self.filhos['btn_save'].grid(column=1, row=0)  # Botao de export arquivo
        self.filhos['btn_del'].grid(column=3, row=0, sticky='e', padx=(10, 10), pady=(10, 10))  # Botao de limpar textos
        self.filhos['cbbox'].grid(column=0, row=1, columnspan=2)  # Combobox de select arquivo


    def get_valores(self, puro):
        valores = {
            'q': self.filhos['edts'][0].get().replace(',', '').split() if puro else self.filhos['edts'][0].get(),
            'e': self.filhos['edts'][1].get().replace(',', '').split() if puro else self.filhos['edts'][1].get(),
            'i': self.filhos['edts'][2].get().replace(',', '').split() if puro else self.filhos['edts'][2].get(),
            'f': self.filhos['edts'][3].get().replace(',', '').split() if puro else self.filhos['edts'][3].get(),
            'p': self.filhos['edts'][4].get(),
            'ft': [elem.replace(',', '').split() for elem in self.filhos['ft'].get('1.0', tk.END).split('\n') if elem != ''] if puro else self.filhos['ft'].get('1.0', tk.END)
        }
        return valores

    def iniciar(self):
        valores = self.get_valores(True)
        auto = self.infos['auto'](valores)

        # auto.print_tupla()
        valid = auto.valida_Tupla()

        if valid == 'Ok':
            self.passos, self.resultado, valores = auto.start()
            self.imgs = desenha_estados(self.passos, valores)
            self.passo_atual = 0
            self.inicia_resultado()
        else:
            messagebox.showerror("Palavra Inválida!", valid)

    def inicia_resultado(self):
        self.pais['result'].grid_rowconfigure(0, weight=1)
        self.pais['result'].grid_columnconfigure(0, weight=1)
        self.pais['result'].grid_columnconfigure(1, weight=1)
        self.pais['result'].grid_columnconfigure(2, weight=1)

        self.pais['result'].grid(column=0, row=4, columnspan=2, sticky='news', padx=(10, 10), pady=(10, 10))
        self.filhos['btn_dir'].grid(column=2, row=0, rowspan=2, sticky='nes', padx=(10, 10), pady=(10, 10))
        self.filhos['btn_esq'].grid(column=0, row=0, rowspan=2, sticky='nws', padx=(10, 10), pady=(10, 10))

        self.muda_labels()
        self.filhos['leg'].grid(column=0, row=0, sticky='nw')
        self.pais['leg'].grid(column=0, row=5, columnspan=2, sticky='news', padx=(10, 10), pady=(10, 10))

    # Salva em um arquivo os valores da interface
    def salvar(self):
        if self.filhos['cbbox'].current() == -1:
            if self.filhos['cbbox'].get().replace(' ', '') != '':
                salvar_auto(self.get_valores(False), self.filhos['cbbox'].get(), self.infos['path_tests'])
            else:
                messagebox.showerror("Erro!", "Escreva um nome válido!")
        elif messagebox.askokcancel('Certeza?', 'Você tem certeza que quer reescrever esse arquivo?'):
            salvar_auto(self.get_valores(False), self.filhos['cbbox'].get(), self.infos['path_tests'])

    # Pega o arquivo salva e insere seus valores na interface
    def insere_salvo(self):
        self.limpar()
        if self.filhos['cbbox'].current() != -1:
            file = get_tests(self.infos['path_tests'])[self.filhos['cbbox'].current()]
            self.filhos['edts'][0].insert(0, file['q'])
            self.filhos['edts'][1].insert(0, file['e'])
            self.filhos['edts'][2].insert(0, file['i'])
            self.filhos['edts'][3].insert(0, file['f'])
            self.filhos['edts'][4].insert(0, file['p'])
            for ft in file['ft']:
                self.filhos['ft'].insert(tk.END, ft)

        else:
            messagebox.showerror("Erro!", "Selecione um item válido!")

    # funcao que muda dinamicamente as imagens  e as labels do resultado
    def muda_labels(self):
        # Label de explicação
        p = self.passos[self.passo_atual]
        self.filhos['exp_img']['text'] = f"Passo: {self.passo_atual}\nEstado atual: {p['ea']}\n" \
                                         f"Palavra restante: {p['rp']}\nLetra analisada: {p['la']}\n" \
                                         f"Próximo estado: {p['pe']}\nRegra utilizada: {p['rt']}\n"

        if self.passo_atual == len(self.passos) - 1:
            self.filhos['exp_img']['text'] += f"\nResultado: {self.resultado}"

        self.filhos['exp_img'].grid(column=1, row=0, sticky='news', padx=(10, 10), pady=(10, 10))

        # Imagem
        self.filhos['img']['image'] = self.imgs[self.passo_atual]
        self.filhos['img'].grid(column=1, row=1, sticky='news', padx=(10, 10), pady=(10, 10))


    # Limpa caixas de texto
    def limpar(self):
        for n in range(5):
            self.filhos['edts'][n].delete(0, 'end')
        self.filhos['ft'].delete('1.0', 'end')

    # Mudam o index dos resultados
    def go_direita(self):
        if self.passo_atual + 1 < len(self.passos):
            self.passo_atual += 1
        else:
            self.passo_atual = 0
        self.muda_labels()

    def go_esquerda(self):
        if self.passo_atual - 1 >= 0:
            self.passo_atual -= 1
        else:
            self.passo_atual = len(self.passos)-1
        self.muda_labels()