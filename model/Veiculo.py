from abc import ABC

class Veiculo(ABC):
    def __init__(self, id, marca, modelo, motor, ano, cor, valor, status = None, quantidade_vendido = 0):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.ano = ano
        self.cor = cor
        self.valor = valor
        self.status = status
        self.quantidade_vendido = quantidade_vendido


    def to_json(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'modelo': self.modelo,
            'motor': self.motor,
            'ano': self.ano,
            'cor': self.cor,
            'valor': self.valor,
            'status': self.status,
            'qtd_vendido': self.quantidade_vendido
        }