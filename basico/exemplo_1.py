def soma(x, y):
    return x + y


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        Pessoa(f'nome={self.nome}, idade={self.idade}')
