from interface.Front_tab import Front
from automatos.AutomatosDeterministicos import AutomatoDeterministico

class AFD_front(Front):
    def __init__(self, janela):
        infos = {
            'auto_exp': 'O que é um Autômato Deterministico?',
            'indc_txt': 'AFD',
            'auto': AutomatoDeterministico
        }
        super().__init__(janela, infos)