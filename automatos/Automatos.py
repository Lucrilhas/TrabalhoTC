
class Automato:
    def __init__(self, Tupla):
        self.Tupla = Tupla

    def print_tupla(self):
        print(f" === Dados gerais do automato ===",
              f" * Estados: {self.Tupla['e']}",
              f" * Alfabeto: {self.Tupla['q']}",
              f" * Estado Inicial: {self.Tupla['i']}",
              f" * Estados Finais: {self.Tupla['f']}",
              f" * Palavra: {self.Tupla['p']}"
              f"\n\n === Regras de transicao ===",
              *self.Tupla['ft'], sep='\n')

    def valida_Tupla(self):
        if len(self.Tupla['q']) == 0:
            return 'Conjunto de estados vazio!'

        for ef in self.Tupla['f']:
            if ef not in self.Tupla['q']:
                return 'Estados finais devem estar no conjunto de estados atingiveis!'

        for regra in self.Tupla['ft']:
            if regra[0] not in self.Tupla['q']:
                return 'Os estados iniciais das regras devem estar no conjunto de estados atingiveis!'

            if regra[1] not in self.Tupla['e']:
                return 'Os simbolos das regras devem estar no alfabeto!'

            if regra[2] not in self.Tupla['q']:
                return 'Os estados alvo das regras devem estar no conjunto de estados atingíveis!'

        return 'Ok'


a = {
        'q': ['q0', 'q1', 'q2', 'qf'],
        'e': ['0', '1'],
        'i': ['q0'],
        'f': ['qf'],
        'p': '010',
        'ft': [
            ['q0', '0', 'q1'],
            ['q1', '1', 'q2'],
            ['q2', '1', 'q1'],
            ['q2', '0', 'qf']
        ]
}

au = Automato(a)
au.print_tupla()
print(au.valida_Tupla())