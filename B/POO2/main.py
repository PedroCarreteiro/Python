class Cachorro():
    #Atributo estático
    qtd_dentes = 32
    def __init__(self, nome, raca, cor, idade):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade

    #Método de classe
    @classmethod
    def criar_cachorro(cls, nome_cls, raca_cls, cor_cls, idade_cls):
        return Cachorro(nome_cls, raca_cls, cor_cls, idade_cls)

    #Método estático
    @staticmethod
    def latir():
        print("Cachorro está latindo")

    def beber_agua(self):
        print(self.nome," está bebendo água")

fred = Cachorro("Fred", "Salsicha", "Preto", 5)

fred.beber_agua()
fred.latir()

