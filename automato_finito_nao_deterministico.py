from automato_finito_deterministico import Afd

class Afn():
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
        print('=' * 30)

    def regras_para_dicionario(self):
        chaves = []
        caminhos = []
        destinos = []

        for regra in self.regras_transicao:
            chaves.append(regra[0])
            caminhos.append(regra[1])
            destinos.append(regra[2])

        lista_dicionarios = []

        for qd in range(len(self.estados)):
            dicio = {}
            for c in caminhos:
                dicio[c] = []
            lista_dicionarios.append(dicio)
        
        afn_dicio = {}
        for indice, estado in enumerate(self.estados):
            afn_dicio[estado] = lista_dicionarios[indice]

        for i, j, k in zip(chaves, caminhos, destinos):
            afn_dicio[i][j].append(k)
        return afn_dicio

    def extrair_regras_dicionario(self, regras_dicio):
        regras_afd = []
        for chave in regras_dicio.keys():
            for chave1 in regras_dicio[chave].keys():
                regras_afd.append([chave, chave1, regras_dicio[chave][chave1]])
        self.regras_transicao = regras_afd.copy()

    def converter_para_afd(self, afn_dicio):
        tam_alfabeto = len(self.alfabeto)
        estados_finais_afn = self.estados_finais          
            
        lista_novos_estados = []                         
        afd = {}                                   
        lista_chaves = list(list(afn_dicio.keys())[0])    
        lista_caminhos = list(afn_dicio[lista_chaves[0]].keys())

        # Calculando a primeira linha da tabela de transição do AFD
        afd[lista_chaves[0]] = {}                   
        for t in range(tam_alfabeto):
            # Criar novo estado
            string_estado = "".join(afn_dicio[lista_chaves[0]][lista_caminhos[t]]) 

            # Atribuir o estado na tabela AFD
            afd[lista_chaves[0]][lista_caminhos[t]] = string_estado  

            # Acrescentar string_estado à lista_chaves e lista_novos_estados          
            if string_estado not in lista_chaves:                         
                lista_novos_estados.append(string_estado)                 
                lista_chaves.append(string_estado)                       
        
        # Calculando as outras linhas da tabela de transição AFD
        while len(lista_novos_estados) != 0:   
            # Pegar o primeiro elemento da lista_novos_estados e fazer sua análise        
            afd[lista_novos_estados[0]] = {} 
            for _ in range(len(lista_novos_estados[0])):
                for i in range(len(lista_caminhos)):
                    lista_temp = []                              
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
        lista_estados_afd = list(afd.keys())
        estados_finais_afd = []
        for eafd in lista_estados_afd:
            for item in eafd:
                if item in estados_finais_afn:
                    estados_finais_afd.append(eafd)
                    break
        
        # Setar valores aos atributos
        self.estados = lista_estados_afd
        self.estados_finais = estados_finais_afd
        self.extrair_regras_dicionario(afd)
        
    def executa_afd(self, palavra):
        # Mostrar dados do automato
        self.mostrar_dados()

        # Criação de um objeto de um automato finito deterministico
        automato = Afd()
        automato.alfabeto = self.alfabeto
        automato.estados = self.estados
        automato.estado_inicial = self.estado_inicial
        automato.estados_finais = self.estados_finais
        automato.regras_transicao = self.regras_transicao
        
        # Validar o automato
        validacao_automato = automato.validar_automato()

        # Fazer leitura da palavra
        if validacao_automato:
            validacao_palavra = automato.ler_palavra(palavra)

            if validacao_palavra:
                print("\n # Palavra valida!")
            else:
                print("\n # Palavra invalida!")
