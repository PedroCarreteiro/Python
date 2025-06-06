class Bolo():
    def __init__(self, recheio: str, cobertura: str, sabor: str = "Chocolate", qtd_fatias: int = 8): #o tipo da variável é apenas para documentar, e não é para ficar apenas esse tipo e bloqeuar
        self.recheio = recheio
        self.sabor = sabor
        self.cobertura = cobertura
        self.qtd_fatias = qtd_fatias
        lista_de_sabores = ["Chcolate", "Morango", "Laranja"]
        if sabor in lista_de_sabores:
            self.sabor = sabor
        else:
            print("Sabor inválido")
        
    def comer_bolo(self):
        print("O bolo de ", self.sabor, " foi comido")
        self.qtd_fatias -= 1
        if self.qtd_fatias <= 0:
            print("O bolo acabou")
        else:
            print(f"O bolo de {self.sabor} com {self.qtd_fatias+1} fatias foi comido e agora tem {self.qtd_fatias}")

    def comer_n_fatias(self, qtd_fatias_comidas):
        if self.qtd_fatias < qtd_fatias_comidas:
            print("Não tem tudo isso de bolo")
        elif self.qtd_fatias == 0:
            print("Não tem bolo")
        else:
            print(qtd_fatias_comidas, "fatia(s) foram comidas do bolo", self.sabor)
            self.qtd_fatias -= qtd_fatias_comidas

bolo_chocolate = Bolo("Chocolate", "Chocolate", "Chocolate", 8)
bolo_morango = Bolo("Morango", "Morango", "Morango", 12)


bolo_laranja = Bolo("Chocolate", "Laranja", "Laranja", 20)

bolo_laranja.comer_n_fatias(18)
print(bolo_laranja.qtd_fatias)

bolo_laranja.comer_n_fatias(1)
print(bolo_laranja.qtd_fatias)





#armazenar a classe dentro da variável
# geladeira = Bolo() 

# print(type(geladeira))

# print(type(Bolo()))