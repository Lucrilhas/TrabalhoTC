import os
import igraph as ig
from PIL import ImageTk, Image

def get_tests(path):
    files = []
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as f:
            files.append({
                'name': filename,
                'e': f.readline().replace('\n', ''),
                'q': f.readline().replace('\n', ''),
                'i': f.readline().replace('\n', ''),
                'f': f.readline().replace('\n', ''),
                'p': f.readline().replace('\n', ''),
                'ft': f.readlines(),
            })
    return files

def salvar_auto(valores, nome, path):
    with open(f'{path}/{nome}.txt', 'w+') as arq:
        for l in valores:
            arq.write(valores[l])


def desenha_estados(passos, vals):
    imgs = []
    g = ig.Graph(directed=True)
    g.add_vertices(vals['q'])
    g.add_edges([v1, v2] for v1, _, v2 in vals['ft'])
    g.vs["label"] = g.vs["name"]
    g.es["label"] = [a for _, a, _ in vals['ft']]

    for n, passo in enumerate(passos):
        n_img = f"imgs/{n}.png"

        visu = {
            'vertex_size': 40,
            'bbox': (700, 700),
            'margin': 50,
            'layout': g.layout("circular"),
            'vertex_label_color': ['white' if v in vals['f'] or v == passo['ea'] else 'black' for v in vals['q']],
            'vertex_color':     ['blue' if v == passo['ea'] else 'red' if v in vals['f'] else 'yellow' for v in vals['q']],
            'edge_width':       [6 if r==passo['rt'] else 2 for r in vals['ft']],
            'edge_arrow_size':  [2 if r==passo['rt'] else 1 for r in vals['ft']],
            'vertex_shape':     ['rectangle' if v in vals['f'] else 'circle' for v in vals['q']]
        }

        ig.plot(g, n_img, **visu)
        img = Image.open(n_img)
        imgs.append(ImageTk.PhotoImage(img))

    return imgs
