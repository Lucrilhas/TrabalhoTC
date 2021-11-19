from automato_finito_deterministico import Afd

if __name__ == '__main__':
    # Instanciacao do objeto
    automato = Afd()

    # Faz a leitura do arquivo
    automato.leitura_arquivo('afd_ramon.txt')

    # Setar valores para a execucao do programa
    automato.set_5upla()

    # Mostrar dados do automato
    automato.mostrar_dados()

    # Validar o automato
    validacao_automato = automato.validar_automato()

    # Fazer leitura da palavra
    if validacao_automato:
        validacao_palavra = automato.ler_palavra("01010")

        if validacao_palavra:
            print("\n # Palavra valida!")
        else:
            print("\n # Palavra invalida!")
