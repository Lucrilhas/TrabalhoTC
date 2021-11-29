self.db = self.db.append({
            'q': ['qo', 'q1', 'q2', 'qf'],
            'e': ['0', '1'],
            'i': ['q0'],
            'f': ['qf'],
            'p': '01110',
            'ft': [
                ['q0', '0', 'q1'],
                ['q1', '1', 'q2'],
                ['q2', '1', 'q1'],
                ['q2', '0', 'qf']
            ],
            'tipo': 'afd'
        }, ignore_index=True)
        self.db.to_csv('automatos/testes/casos.csv', index=False)