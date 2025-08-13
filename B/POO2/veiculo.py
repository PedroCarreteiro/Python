class Veiculo:
    def __init__(self, marca, nivel_tank):
        self.marca = marca
        self.nivel_tank = nivel_tank

    def abastecer(self):
        print("O veículo está abastecendo, segue o nível do tank: ", self.nivel_tank)

class Carro(Veiculo):
    def __init__(self, marca, nivel_tank, qtd_portas):
        super().__init__(marca, nivel_tank)
        self.qtd_portas = qtd_portas

class Civic(Carro):
    pass

class Moto(Veiculo):
    pass

veiculo1 = Veiculo("Mercedes" , 100)

carro1 = Carro("Honda", 150, 4)

carro1.abastecer()

