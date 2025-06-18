class Trator():
    def __init__(self, marca = str, modelo = str, potencia = int, tipo_roda = str, combustivel = bool, tempo_trabalhado = int, situacao_motor = str, rodado: bool = True):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.tipo_roda = tipo_roda
        self.combustivel = combustivel
        self.__tempo_trabalhado = tempo_trabalhado
        self.__situacao_motor = situacao_motor
        self.rodado = rodado

        if combustivel.lower() == "sim":
            self.combustivel = True
        else:
            self.combustivel = False

        tipos_de_roda = ["simples","duplo","esteira"]
        if tipo_roda.lower() in tipos_de_roda:
            self.rodado = True
            self.tipo_roda = tipo_roda
        else:
            self.rodado = False
            print("Rodado inválido!")

        situacoes_motor = ["ruim","conservado","novo"]
        if self.__situacao_motor.lower() in situacoes_motor:
            self.__situacao_motor = situacao_motor
        else:
            print("Estado do motor inválido!")
        

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
            opcao = input("Trator sem combustivel, você gostaria de reabastece-lo? ")
            if opcao.lower() == "sim":
                self.reabastecer()
                self.imprimir_aradura()
            else:
                print("Trator continua sem combustível!")

    def get_tempo_trabalhado(self):
        print(f"O tempo trabalhado do trator é {self.__tempo_trabalhado}")
        return self.__tempo_trabalhado
    
    def set_tempo_trabalhado(self, tempo_atualizado):
        self.__tempo_trabalhado = tempo_atualizado
        self.get_tempo_trabalhado()

    def get_situacao_motor(self):
        print(f"A situação atual do motor é {self.__situacao_motor}")
        return self.__situacao_motor
    
    def set_situacao_motor(self, situacao_atualizada):
        situacoes_motor = ["ruim","conservado","novo"]
        if situacao_atualizada.lower() in situacoes_motor:
            self.__situacao_motor = situacao_atualizada.lower()
            self.get_situacao_motor()
        else:
            print("Essa situação está indisponível!")
            
    def __consertar_motor(self):
        situacoes_motor = ["ruim","conservado","novo"]
        if (self.__situacao_motor.lower() == "ruim") or (self.__situacao_motor.lower() == "conservado"):
            posicao_situacao = situacoes_motor.index(self.__situacao_motor.lower())
            print("Motor consertado!")
            self.set_situacao_motor(situacoes_motor[posicao_situacao+1])
        else:
            print("Motor não pode ser consertado!")

    def revisao(self):
        self.__consertar_motor()
        print("A revisão foi realizada com sucesso!")

# trator = Trator(
#     input("Digite a marca do trator: "),
#     input("Digite o modelo do trator: "),
#     int(input("Digite a potência do trator: ")),
#     input("Qual o seu tipo de rodado? "),
#     input("O trator tem combustível? "),
#     input("Qual o seu tempo trabalhado? "),
#     input("Qual a situação do motor? ")
# )

# if trator.rodado:
#     if trator.combustivel.lower() == "sim":
#         trator.combustivel = True
#     else:
#         trator.combustivel = False
#         opcao_reabastecer = input("Você quer reabastecer o trator? ")

#         if opcao_reabastecer.lower() == "sim":
#             trator.reabastecer()
#             print(trator.combustivel)
#         else:
#             print("Trator sem reabastecimento!")

#     opcao_arar = input("Você quer arar o campo? ")

#     if opcao_arar.lower() == "sim":
#         trator.arar_campo()
#     else:
#         print("Campo continua sem aradura!")


trator = Trator(
    "John Deere",
    "8R",
    270,
    "Simples",
    "Sim",
    170,
    "Ruim"
)

trator.get_tempo_trabalhado()
trator.set_tempo_trabalhado(180)
trator.get_situacao_motor()
trator.set_situacao_motor("C1nservado")
trator.revisao()





