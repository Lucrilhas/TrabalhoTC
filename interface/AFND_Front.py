from automatos.AutomatosNDeterministicos import AutomatoNDeterministico
from interface.Front_tab import Front


class AFND_front(Front):
    def __init__(self, janela):
        infos = {
            'auto_exp': 'O que é um Autômato não-Deterministico?',
            'indc_txt': 'AFND',
            'auto': AutomatoNDeterministico
        }
        super().__init__(janela, infos)