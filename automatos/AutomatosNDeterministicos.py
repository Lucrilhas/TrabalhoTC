from automatos.AutomatosDeterministicos import AutomatoDeterministico

class AutomatoNDeterministico(AutomatoDeterministico):
    def __init__(self, Tupla):
        super().__init__(Tupla)

    def regras_para_dicionario(self):
        chaves = []
        caminhos = []
        destinos = []

        for regra in self.tupla['ft']:
            chaves.append(regra[0])
            caminhos.append(regra[1])
            destinos.append(regra[2])

        lista_dicionarios = []

        for qd in range(len(self.tupla['q'])):
            dicio = {}
            for c in caminhos:
                dicio[c] = []
            lista_dicionarios.append(dicio)

        afn_dicio = {}
        for indice, estado in enumerate(self.tupla['q']):
            afn_dicio[estado] = lista_dicionarios[indice]

        for i, j, k in zip(chaves, caminhos, destinos):
            afn_dicio[i][j].append(k)
        return afn_dicio

    def extrair_regras_dicionario(self, regras_dicio):
        regras_afd = []
        for chave in regras_dicio.keys():
            for chave1 in regras_dicio[chave].keys():
                regras_afd.append([chave, chave1, regras_dicio[chave][chave1]])

        inconsistentes = []
        for regra in regras_afd:
            if not len(regra[2]):
                inconsistentes.append(regra)
        for item in inconsistentes:
            regras_afd.remove(item)

        self.tupla['ft'] = regras_afd.copy()

    def converter_para_afd(self, afn_dicio):
        tam_alfabeto = len(self.tupla['e'])
        estados_finais_afn = self.tupla['f']

        lista_novos_estados = []
        afd = {}
        lista_chaves = list(list(afn_dicio.keys())[0])
        lista_caminhos = list(afn_dicio[lista_chaves[0]].keys())

        # Calculando a primeira linha da tabela de transição do AFD
        afd[lista_chaves[0]] = {}
        for t in range(tam_alfabeto):
            # Criar novo estado (junta o nome dos estados referentes a uma possibilidade)
            string_estado = "".join(afn_dicio[lista_chaves[0]][lista_caminhos[t]])

            # Atribuir o estado na tabela AFD
            afd[lista_chaves[0]][lista_caminhos[t]] = string_estado

            # Acrescentar string_estado à lista_chaves e lista_novos_estados
            # caso a string estado não esteja na lista de chaves
            if string_estado not in lista_chaves:
                lista_novos_estados.append(string_estado)
                lista_chaves.append(string_estado)

                # Calculando as outras linhas da tabela de transição AFD
        while len(lista_novos_estados) != 0:
            # Pegar o primeiro elemento da lista_novos_estados e fazer sua análise
            afd[lista_novos_estados[0]] = {}

            # Percorre a string na posição 0 dos novos estados
            for _ in range(len(lista_novos_estados[0])):
                # Percorre a lista de caminhos
                for i in range(len(lista_caminhos)):
                    lista_temp = []
                    # Percorre a string na posição 0 dos novos estados para
                    # a criação dos outros estados
                    for j in range(len(lista_novos_estados[0])):
                        # União dos estados
                        lista_temp += afn_dicio[lista_novos_estados[0][j]][lista_caminhos[i]]

                        # Cria um novo estado de todos os elementos da lista
                    string_estado = ""
                    string_estado = string_estado.join(lista_temp)

                    # Acrescentar string_estado à lista_chaves e lista_novos_estados
                    if string_estado not in lista_chaves:
                        lista_novos_estados.append(string_estado)
                        lista_chaves.append(string_estado)

                        # Atribuir o novo estado na tabela AFD
                    afd[lista_novos_estados[0]][lista_caminhos[i]] = string_estado

                    # Remover o primeiro elemento em lista_novos_estados
            lista_novos_estados.remove(lista_novos_estados[0])

        # Estados finais do AFD
        lista_estados_afd = [estado for estado in list(afd.keys()) if estado != '']
        estados_finais_afd = []

        for eafd in lista_estados_afd:
            for item in eafd:
                if item in estados_finais_afn:
                    estados_finais_afd.append(eafd)
                    break

        # Setar valores aos atributos
        self.extrair_regras_dicionario(afd)
        self.tupla['q'] = lista_estados_afd.copy()
        self.tupla['f'] = estados_finais_afd.copy()

    def executa_afd(self):
        # Criação de um objeto de um automato finito deterministico
        automato = AutomatoDeterministico(self.tupla)
        # automato.print_tupla()
        saida = automato.start()
        return saida

    def start(self):
        afn_dicio = self.regras_para_dicionario()
        self.converter_para_afd(afn_dicio)
        p, m, t= self.executa_afd()
        return p, m, t
