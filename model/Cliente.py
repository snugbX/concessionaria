class Cliente:
    def __init__(self, nome, cpf, senha, compras=None):
        self.compras = compras
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

    def add_compra(self, compra):
        self.compras.append(compra)

    def to_json(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'senha': self.senha,
            'compras': self.compras
        }