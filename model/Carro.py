from model.Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, id, marca, modelo, motor, ano, cor, valor):
        super(Carro, self).__init__(id, marca, modelo, motor, ano, cor, valor)

    def to_json(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'modelo': self.modelo,
            'motor': self.motor,
            'ano': self.ano,
            'cor': self.cor,
            'valor': self.valor,
            'status': self.status
        }