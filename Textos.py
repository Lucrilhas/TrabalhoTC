txts = {
    'Guias': [
        # 'Teste',
        'Deterministico',
        'Não Deterministico',
        # 'Deterministico de Pilha',
        # 'Não Deterministicos de Pilha'

    ],

    'AFD': 'Um autômato finito determinístico, também chamado máquina de estados finita determinística (AFD), '
           'É uma máquina\nde estados finita que aceita ou rejeita cadeias de símbolos gerando um único ramo de '
           'computação para cada cadeia de\nentrada. Estas sendo configuradas em um tipo chamado de 5-Tupla.',

    'AFND': 'Um autômato finito não determinístico, também chamado máquina de estados finita não determinística (AFND),\n'
           'é uma máquina de estados finita que pode diferente das AFDs, aceitar diversos estados possíveis.\n'
            'Embora sejam diferentes, é provado que toda AFND é também uma AFD e também o contrário.',

    'EXP_5T': 'Uma 5-Tupla P = { Q, \u03A3, \u03B4, q\u2080, F }.\n'
                 'Sendo \' Q \' o conjunto de estados.\n'
                 'Sendo \' \u03A3 \' o alfabeto de entradas.\n'
                 'Sendo \' \u03B4 : Q \u2613 \u03A3\u2091 \u2613 P(Q) \' a função de  transição.\n'
                 'Sendo \' q\u2080 \u2208 Q \' o estado inicial.\n'
                 'Sendo \' F \u2286 Q \' é o conjunto de estados finais.',

    'VAL_5T': [
        'Conjunto de estados Q: ',
        'Alfabeto de entradas \u03A3: ',
        'Estado inicial q\u2080',
        'Estados Finais F: ',
        'Palavra para testar:'
    ],

    'LEG': 'Vértices amarelos\t\u2192 Vértices comuns que não estão sendo utilizados.\n'
           'Vértices azuis\t\u2192 Vértice da posição no passo.\n'
           'Vértices vermelho\t\u2192 Vértices de estados finais\n'
           'Aresta grossa\t\u2192 Regra utilizada no passo\n'
           'Valor aresta\t\u2192 Valor de entrada da regra.'
}
