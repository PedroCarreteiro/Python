class Campo():
    def __init__(self, aradura = bool):
        self.aradura = aradura

class Trator():
    def __init__(self, marca = str, modelo = str, potencia = int, tipo_roda = str, combustivel = bool, rodado: bool = True):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.tipo_roda = tipo_roda
        self.combustivel = combustivel
        self.rodado = rodado
        tipos_de_roda = ["simples","duplo","esteira"]
        if tipo_roda.lower() in tipos_de_roda:
            self.rodado = True
            self.tipo_roda = tipo_roda
        else:
            self.rodado = False
            print("Rodado inválido!")
        

    def reabastecer(self):
        self.combustivel = True
        print("Trator reabastecido!")

    def imprimir_aradura(self):
        if self.tipo_roda.lower() == "esteira":
            print("O campo foi arado e o solo foi levemente compactado!")
        elif self.tipo_roda.lower() == "duplo":
            print("O campo foi arado e o solo foi compactado de forma mediana!")
        elif self.tipo_roda.lower() == "simples":
            print("O campo foi arado e o solo foi muito compactado!")

    def arar_campo(self):
        if self.combustivel == True:
            self.combustivel = False
            self.imprimir_aradura()
        else:
            opcao = input("Trator sem combustvel, você gostaria de reabastece-lo? ")
            if opcao.lower() == "sim":
                self.reabastecer()
                self.imprimir_aradura()
            else:
                print("Trator continua sem combustível!")
        

trator = Trator(
    input("Digite a marca do trator: "),
    input("Digite o modelo do trator: "),
    input("Digite a potência do trator: "),
    input("Qual o seu tipo de rodado? "),
    input("O trator tem combustível? ")
)

if trator.rodado:
    if trator.combustivel.lower() == "sim":
        trator.combustivel = True
    else:
        trator.combustivel = False
        opcao_reabastecer = input("Você quer reabastecer o trator? ")

        if opcao_reabastecer.lower() == "sim":
            trator.reabastecer()
            print(trator.combustivel)
        else:
            print("Trator sem reabastecimento!")

    opcao_arar = input("Você quer arar o campo? ")

    if opcao_arar.lower() == "sim":
        trator.arar_campo()
    else:
        print("Campo continua sem aradura!")
