from bk.automato_finito_nao_deterministico import Afn

if __name__ == '__main__':
    # Instanciacao do objeto
    automato_afn = Afn()

    # Faz a leitura do arquivo
    automato_afn.leitura_arquivo('testes/testes_afn/afn1.txt')

    # Setar valores para a execucao do programa
    automato_afn.set_5upla()

    # Mostrar dados do automato
    # automato_afn.mostrar_dados()

    afn_dicio = automato_afn.regras_para_dicionario()
    automato_afn.converter_para_afd(afn_dicio)
    automato_afn.executa_afd('abababa')

#010100
#abababa