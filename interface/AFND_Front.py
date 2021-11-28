from interface.Front_tab import Front
from automatos.AutomatosNDeterministicos import AutomatoNDeterministico

class AFND_front(Front):
    def __init__(self, janela):
        infos = {
            'auto_exp': 'O que é um Autômato não-Deterministico?',
            'indc_txt': 'AFND',
            'path_tests': 'automatos/testes/testes_afn',
            'auto': AutomatoNDeterministico
        }
        super().__init__(janela, infos)