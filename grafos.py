import igraph as ig

class DesenhaAutomato:
    def __init__(self, op):
        self.op = op
        self.g = ig.Graph(directed=True)
        self.g.add_vertices(op['q'])
        # self.g.degree(mode="in")
        self.g.add_edges([v1, v2] for v1, _, v2 in op['ft'])
        self.g.vs["label"] = self.g.vs["name"]
        self.g.es["label"] = [a for _, a, _ in op['ft']]

    def plota(self, nome_arq):
        visu = {
            'vertex_size': 40,
            'bbox': (900, 900),
            'margin': 20,
            # layout: auto,
            'edge_width': [3 for _ in enumerate(self.op['ft'])],
            'vertex_color': ['red' if c in self.op['F'] else 'yellow' for c in self.op['q']],
            'vertex_shape': ['rectangle' if c in self.op['f'] else 'circle' for c in self.op['q']],
            'vertex_label_color': ['white' if c in self.op['f'] else 'black' for c in self.op['q']],
            'edge_arrow_size': 2
        }
        ig.plot(self.g, nome_arq, **visu)






dados = {
            'Q': ['q0', 'q1', 'q2', 'qf'],
            'E': ['0', '1'],
            'q': ['q0'],
            'F': ['qf'],
            'P': '01110',
            'FT': [
                ['q0', '0', 'q1'],
                ['q1', '1', 'q2'],
                ['q2', '1', 'q1'],
                ['q2', '0', 'qf']
            ]
}
dg = DesenhaAutomato(dados)
dg.plota('imgs/aaa.png')