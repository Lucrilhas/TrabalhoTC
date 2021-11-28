from interface.Front_tab import Front
from automatos.automato_finito_deterministico import Afd

class AFND_front(Front):
    def __init__(self, janela):
        infos = {
            'auto_exp': 'O que é um Autômato não-Deterministico?',
            'indc_txt': 'AFND',
            'path_tests': 'automatos/testes/testes_afn',
            'auto': Afd()
        }
        super().__init__(janela, infos)