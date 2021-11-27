class Afd:
    def __init__(self):

        self.dados = None
    
    def leitura_arquivo(self, nome_arquivo, palavra):
        with open(nome_arquivo, 'r') as arquivo:
            dados_automato = [linha.split(',') for linha in [linha.replace('\n', '') for linha in arquivo]]
            self.dados = {
                'Q': dados_automato[1],
                'E': dados_automato[0],
                'q': dados_automato[2],
                'F': dados_automato[3],
                'P': palavra,
                'FT': dados_automato[4:].copy()
            }
        
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

    # def ler_palavra(self):
    #     passo_passo = {}
    #     estado_atual = self.dados['i'][0]
    #     saida = ''
    #
    #     for i, letra in enumerate(self.dados['p']):
    #         estado_validacao = False
    #
    #         for regra in self.dados['ft']:
    #             if (regra[0] == estado_atual) and (regra[1] == letra):
    #                 aux = self.dados['p'][i:]
    #                 saida += f' - Estado atual: {estado_atual} | Restante palavra: {aux} | Para o estado: {regra[2]}\n'
    #                 estado_atual = regra[2]
    #                 estado_validacao = True
    #                 passo_passo[i] = estado_atual
    #                 break
    #
    #         if not estado_validacao:
    #             return '\n # Palavra invalida!'
    #
    #     if estado_atual in self.dados['f']:
    #         return saida + '\n # Palavra valida!'
    #     else:
    #         return '\n # Palavra invalida!'

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
                        'pe': regra[2],             # pe = proximo estado
                        'rt': regra                 # rt = regra de transição utilizada
                    })
                    estado_atual = regra[2]
                    estado_validacao = True
                    break
            if not estado_validacao:
                return passos, 'Palavra inválida!'

        if estado_atual in self.dados['f']:
            return passos, 'Palavra válida!'
        else:
            return passos, 'Palavra inválida!'