class Afd():
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
        print(f" * Alfabeto: {self.dados['E']}")
        print(f" * Estados: {self.dados['Q']}")
        print(f" * Estado Inicial: {self.dados['q']}")
        print(f" * Estados Finais: {self.dados['F']}")
        print(f" * Palavra: {self.dados['P']}")

        print("\n === Regras de transicao ===\n")
        for regra in self.dados['FT']:
            print(' - ', regra)

    def validar_automato(self):
        if len(self.dados['Q']) == 0:
            print("\n # Conjunto de estados vazio!")
            return False

        for ef in self.dados['F']:
            if ef not in self.dados['Q']:
                print("\n # Estados finais devem estar no conjunto de estados atingiveis!")
                return False

        for regra in self.dados['FT']:
            if regra[0] not in self.dados['Q']:
                print("\n # Os estados iniciais das regras devem estar no conjunto de estados atingiveis!")
                return False

            if regra[1] not in self.dados['E']:
                print("\n # Os simbolos das regras devem estar no alfabeto!")
                return False

            if regra[2] not in self.dados['Q']:
                print("\n # Os estados alvo das regras devem estar no conjunto de estados atingíveis!")
                return False

        return True

    def ler_palavra(self):
        estado_atual = self.dados['q'][0]
        print("\n === Inicio do processamento do automato === \n")

        for i, letra in enumerate(self.dados['P']):
            estado_validacao = False

            for regra in self.dados['FT']:
                if (regra[0] == estado_atual) and (regra[1] == letra):
                    print(f" - Estado atual: {estado_atual}", end=' ')
                    print(f"| Restante palavra: {self.dados['P'][i:]}", end=' ')
                    print(f"| Para o estado:", regra[2])
                    estado_atual = regra[2]
                    estado_validacao = True
                    break

            if not estado_validacao:
                return False

        if estado_atual in self.dados['F']:
            return True
        else:
            return False
