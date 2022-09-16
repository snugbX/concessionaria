class Venda:
    def __init__(self, nome_cliente, cpf_cliente, produto, valor_total , data_venda, desconto = 0.0):
        self.nome_cliente = nome_cliente
        self.cpf_cliente = cpf_cliente
        self.produto = produto
        self.valor_total = valor_total
        self.data_venda = data_venda
        self.desconto = desconto


    def to_JSON(self):
        return {
            'nome_cliente': self.nome_cliente,
            'cpf_cliente' : self.cpf_cliente,
            'produto' : self.produto,
            'valor_total' : self.valor_total,
            'data_venda' : self.data_venda
        }

    def calcula_desconto(self):
        if self.desconto > 0:
            self.valor_total = self.valor_total - (self.produto['valor']*(self.desconto/100))
        else:
            print("Não foi aplicado nenhum desconto")
            self.valor_total = self.produto['valor']
