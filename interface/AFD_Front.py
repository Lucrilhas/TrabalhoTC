from interface.Front_tab import Front
from automatos.automato_finito_deterministico import Afd

class AFD_front(Front):
    def __init__(self, janela):
        infos = {
            'auto_exp': 'O que é um Autômato Deterministico?',
            'indc_txt': 'AFD',
            'path_tests': 'automatos/testes/testes_afd',
            'auto': Afd()
        }
        super().__init__(janela, infos)