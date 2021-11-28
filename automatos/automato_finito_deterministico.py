class Afd:
    def __init__(self):

        self.dados = None
        
    def set_5upla(self, dados):
        self.dados = dados

    def mostrar_dados(self):
        print(" === Dados gerais do automato ===\n")
        print(f" * Alfabeto: {self.dados['e']}")
        print(f" * Estados: {self.dados['q']}")
        print(f" * Estado Inicial: {self.dados['i']}")
        print(f" * Estados Finais: {self.dados['f']}")
        print(f" * Palavra: {self.dados['p']}")

        print("\n === Regras de transicao ===\n")
        for regra in self.dados['ft']:
            print(' - ', regra)

    def validar_automato(self):
        if len(self.dados['q']) == 0:
            return 'Conjunto de estados vazio!'

        for ef in self.dados['f']:
            if ef not in self.dados['q']:
                return 'Estados finais devem estar no conjunto de estados atingiveis!'

        for regra in self.dados['ft']:
            if regra[0] not in self.dados['q']:
                return 'Os estados iniciais das regras devem estar no conjunto de estados atingiveis!'

            if regra[1] not in self.dados['e']:
                return 'Os simbolos das regras devem estar no alfabeto!'

            if regra[2] not in self.dados['q']:
                return 'Os estados alvo das regras devem estar no conjunto de estados atingíveis!'

        return 'Ok'

    def processa_palavra(self):
        passos = []
        estado_atual = self.dados['i'][0]

        for i, letra in enumerate(self.dados['p']):
            estado_validacao = False

            for regra in self.dados['ft']:
                if (regra[0] == estado_atual) and (regra[1] == letra):
                    passos.append({
                        'ea': estado_atual,         # ea = estado atual
                        'rp': self.dados['p'][i:],  # rp = restante palavra
                        'la': self.dados['p'][i],  # la = letra analisada
                        'pe': regra[2],             # pe = proximo estado
                        'rt': regra                 # rt = regra de transição utilizada
                    })
                    estado_atual = regra[2]
                    estado_validacao = True
                    break
            if not estado_validacao:
                passos.append({
                    'ea': estado_atual,         # ea = estado atual
                    'rp': self.dados['p'][i:],  # rp = restante palavra
                    'la': self.dados['p'][i],  # la = letra analisada
                    'pe': 'não há',             # pe = proximo estado
                    'rt': 'não há'                 # rt = regra de transição utilizada
                    })
                return passos, 'Palavra inválida!\nNão há regra no estado atual que aceite essa entrada!'

        if estado_atual in self.dados['f']:
            return passos, 'Palavra válida!'
        else:
            passos.append({
                'ea': estado_atual,  # ea = estado atual
                'rp': 'Acabou',  # rp = restante palavra
                'la': 'Não há', # la = letra analisada
                'pe': 'Não há',  # pe = proximo estado
                'rt': 'Não há'  # rt = regra de transição utilizada
            })
            return passos, 'Palavra inválida!\nA linguagem acabou em um estado não final!'