class Afd():
    def __init__(self):
        self.alfabeto = None
        self.estados = None
        self.estado_inicial = None
        self.estados_finais = None
        self.regras_transicao = None
        self.automato = None
    
    def leitura_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            self.automato = [linha.replace('\n', '') for linha in arquivo]
        
    def set_5upla(self):
        dados_automato = [linha.split(',') for linha in self.automato]
        self.alfabeto = dados_automato[0]
        self.estados = dados_automato[1]
        self.estado_inicial = dados_automato[2]
        self.estados_finais = dados_automato[3]
        self.regras_transicao = dados_automato[4:].copy()

    def mostrar_dados(self):
        print(" === Dados gerais do automato ===\n")
        print(f" * Alfabeto: {self.alfabeto}")
        print(f" * Estados: {self.estados}")
        print(f" * Estado Inicial: {self.estado_inicial}")
        print(f" * Estados Finais: {self.estados_finais}")

        print("\n === Regras de transicao ===\n")
        for regra in self.regras_transicao:
            print(' - ', regra)

    def validar_automato(self):
        if len(self.estados) == 0:
            print("\n # Conjunto de estados vazio!")
            return False

        for ef in self.estados_finais:
            if ef not in self.estados:
                print("\n # Estados finais devem estar no conjunto de estados atingiveis!")
                return False

        for regra in self.regras_transicao:
            if regra[0] not in self.estados:
                print("\n # Os estados iniciais das regras devem estar no conjunto de estados atingiveis!")
                return False

            if regra[1] not in self.alfabeto:
                print("\n # Os simbolos das regras devem estar no alfabeto!")
                return False

            if regra[2] not in self.estados:
                print("\n # Os estados alvo das regras devem estar no conjunto de estados atingíveis!")
                return False

        return True

    def ler_palavra(self, palavra):
        estado_atual = self.estado_inicial[0]
        print("\n === Inicio do processamento do automato === \n")

        for i, letra in enumerate(palavra):
            estado_validacao = False

            for regra in self.regras_transicao:
                if (regra[0] == estado_atual) and (regra[1] == letra):
                    print(f" - Estado atual: {estado_atual}", end=' ')
                    print(f"| Restante palavra: {palavra[i:]}", end=' ')
                    print(f"| Para o estado:", regra[2])
                    estado_atual = regra[2]
                    estado_validacao = True
                    break

            if not estado_validacao:
                return False

        if estado_atual in self.estados_finais:
            return True
        else:
            return False
