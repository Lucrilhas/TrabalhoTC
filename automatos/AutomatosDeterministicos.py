
class AutomatoDeterministico:
    def __init__(self, Tupla):
        self.tupla = Tupla

    def print_tupla(self):
        print(f" === Dados gerais do automato ===",
              f" * Estados: {self.tupla['q']}",
              f" * Alfabeto: {self.tupla['e']}",
              f" * Estado Inicial: {self.tupla['i']}",
              f" * Estados Finais: {self.tupla['f']}",
              f" * Palavra: {self.tupla['p']}"
              f"\n\n === Regras de transicao ===",
              *self.tupla['ft'], sep='\n')

    def valida_Tupla(self):
        if len(self.tupla['q']) == 0:
            return 'Conjunto de estados vazio!'

        for ef in self.tupla['f']:
            if ef not in self.tupla['q']:
                return 'Estados finais devem estar no conjunto de estados atingiveis!'

        for regra in self.tupla['ft']:
            if regra[0] not in self.tupla['q']:
                return 'Os estados iniciais das regras devem estar no conjunto de estados atingiveis!'

            if regra[1] not in self.tupla['e']:
                return 'Os simbolos das regras devem estar no alfabeto!'

            if regra[2] not in self.tupla['q']:
                return 'Os estados alvo das regras devem estar no conjunto de estados atingíveis!'

        return 'Ok'

    def processa_palavra(self):
        passos = []
        estado_atual = self.tupla['i'][0]

        for i, letra in enumerate(self.tupla['p']):
            estado_validacao = False

            for regra in self.tupla['ft']:
                if (regra[0] == estado_atual) and (regra[1] == letra):
                    passos.append({
                        'ea': estado_atual,         # ea = estado atual
                        'rp': self.tupla['p'][i:],  # rp = restante palavra
                        'la': self.tupla['p'][i],  # la = letra analisada
                        'pe': regra[2],             # pe = proximo estado
                        'rt': regra                 # rt = regra de transição utilizada
                    })
                    estado_atual = regra[2]
                    estado_validacao = True
                    break
            if not estado_validacao:
                passos.append({
                    'ea': estado_atual,         # ea = estado atual
                    'rp': self.tupla['p'][i:],  # rp = restante palavra
                    'la': self.tupla['p'][i],  # la = letra analisada
                    'pe': 'não há',             # pe = proximo estado
                    'rt': 'não há'                 # rt = regra de transição utilizada
                    })
                return passos, 'Palavra inválida!\nNão há regra no estado atual que aceite essa entrada!'

        if estado_atual in self.tupla['f']:
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



    def start(self):
        p, m = self.processa_palavra()
        return p, m, self.tupla
