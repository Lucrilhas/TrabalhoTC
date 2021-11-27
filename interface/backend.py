import os
import igraph as ig
from PIL import ImageTk, Image

def get_afd_tests():
    files = []
    for filename in os.listdir('automatos/testes/testes_afd'):
        with open(os.path.join('automatos/testes/testes_afd', filename), 'r') as f:
            files.append({
                'name': filename,
                'e': f.readline(),
                'q': f.readline(),
                'i': f.readline(),
                'f': f.readline(),
                'ft': f.readlines(),
            })

    return files

def salvar_afd(valores, nome):
    with open(f'automatos/testes/testes_afd/{nome}.txt', 'w+') as arq:
        for l in valores:
            arq.write(valores[l])


def desenha_estados(passos, vals):
    imgs = []
    g = ig.Graph(directed=True)
    g.add_vertices(vals['q'])
    g.add_edges([v1, v2] for v1, _, v2 in vals['ft'])
    g.vs["label"] = g.vs["name"]
    g.es["label"] = [a for _, a, _ in vals['ft']]

    print(vals)
    print(passos[0])

    for n, passo in enumerate(passos):
        n_img = f"imgs/{n}.png"

        visu = {
            'vertex_size': 40,
            'bbox': (700, 700),
            'margin': 20,
            # layout: auto,
            # 'edge_width': [4 if c in passo['ea'] else 2 for c in vals['ft'][0]],
            # 'edge_arrow_size': 2
            # 'vertex_shape': ['rectangle' if c in vals['f'] else 'circle' for c in vals['q']],
            # 'vertex_label_color': ['white' if c in vals['f'] else 'black' for c in vals['q']],
            # 'vertex_color': ['red' if c in vals['f'] else 'yellow' for c in vals['q']],
            'vertex_color': ['blue' if v == passo['ea'] else 'red' if v in vals['f'] else 'yellow' for v in vals['q']]
        }

        ig.plot(g, n_img, **visu)
        img = Image.open(n_img)
        imgs.append(ImageTk.PhotoImage(img))

    return imgs
