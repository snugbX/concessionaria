from model.Veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, id, marca, modelo, motor, ano, cor, valor, status):
        super(Moto, self).__init__(id, marca, modelo, motor, ano, cor, valor, status)

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