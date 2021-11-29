import os
import igraph as ig
from PIL import ImageTk, Image
import pandas as pd



class BackEnd():
    def __init__(self):
        self.db = pd.read_csv('automatos/casos.csv')

    def insere_valor(self, valores, origem, nome):
        if nome not in self.db['nome'].values:
            valores['tipo'] = origem
            valores['nome'] = nome
            valores['p'] = f"'{valores['p']}'"
            self.db = self.db.append(valores, ignore_index=True)
            self.db.to_csv('automatos/casos.csv', index=False)

    def get_valores(self, tipo):
        return [dic for dic in pd.read_csv('automatos/casos.csv').to_dict('records') if dic['tipo'] == tipo]


            

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