import os

def validar_entrada_afd(entradas):
    pass

def get_afd_tests():
    files = []
    for filename in os.listdir('automatos/testes/testes_afd'):
        with open(os.path.join('automatos/testes/testes_afd', filename), 'r') as f:
            files.append({
                'name': filename,
                'Q': f.readline().replace('\n', ''),
                'E': f.readline().replace('\n', ''),
                'i': f.readline().replace('\n', ''),
                'f': f.readline().replace('\n', ''),
                'ft': f.readlines(),
            })

    return files
