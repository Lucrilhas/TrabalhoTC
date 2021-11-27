import os

def get_afd_tests():
    files = []
    for filename in os.listdir('automatos/testes/testes_afd'):
        with open(os.path.join('automatos/testes/testes_afd', filename), 'r') as f:
            files.append({
                'name': filename,
                'q': f.readline(),
                'e': f.readline(),
                'i': f.readline(),
                'f': f.readline(),
                'ft': f.readlines(),
            })

    return files

def salvar_afd(valores, nome):
    with open(f'automatos/testes/testes_afd/{nome}.txt', 'w+') as arq:
        for l in valores:
            arq.write(valores[l])