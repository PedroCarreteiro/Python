codigo_produto1 = 1
codigo_produto2 = 2
codigo_produto3 = 3
codigo_produto4 = 4
codigo_produto5 = 5

preco_produto1 = 5.00
preco_produto2 = 3.50
preco_produto3 = 4.80
preco_produto4 = 8.90
preco_produto5 = 7.32

nome_produto1 = "Chocolate"
nome_produto2 = "Manteiga"
nome_produto3 = "Laranja"
nome_produto4 = "Nescau"
nome_produto5 = "Dolly Guaraná"

nome = input("Olá, seja bem vindo ao nosso mercado!"
             "\nDigite o seu nome: ")

escolha = int(input(f"\nBem vindo {nome}!\n"
                    f"Temos os seguintes produtos:\n"
                    f" Código  |      Nome      | Preço\n"
                    f"    1    | Chocolate      | 5.00\n"
                    f"    2    | Manteiga       | 3.50\n"
                    f"    3    | Laranja        | 4.80\n"
                    f"    4    | Nescau         | 8.90\n"
                    f"    5    | Dolly Guaraná  | 7.32\n"
                    f"Digite o código do produto de sua escolha: "))

if escolha == 1:
    quantidade = int(input(f"\nMuito bem! O {nome_produto1} está R${preco_produto1:.2f}"
                           f"\nQuantas unidades você vai querer: "))
    total = quantidade * preco_produto1
    print(f"\nO total da sua compra de {nome_produto1}, com {quantidade} unidades, ficou R${total:.2f}!")
    print(f"\nVolte sempre!")

elif escolha == 2:
    quantidade = int(input(f"\nMuito bem! A {nome_produto2} está R${preco_produto2:.2f}"
                           f"\nQuantas unidades você vai querer: "))
    total = quantidade * preco_produto2
    print(f"\nO total da sua compra de {nome_produto2}, com {quantidade} unidades, ficou R${total:.2f}!")
    print(f"\nVolte sempre!")

elif escolha == 3:
    quantidade = int(input(f"\nMuito bem! A {nome_produto3} está R${preco_produto3:.2f}"
                           f"\nQuantas unidades você vai querer: "))
    total = quantidade * preco_produto3
    print(f"\nO total da sua compra de {nome_produto3}, com {quantidade} unidades, ficou R${total:.2f}!")
    print(f"\nVolte sempre!")

elif escolha == 4:
    quantidade = int(input(f"\nMuito bem! O {nome_produto4} está R${preco_produto4:.2f}"
                           f"\nQuantas unidades você vai querer: "))
    total = quantidade * preco_produto4
    print(f"\nO total da sua compra de {nome_produto4}, com {quantidade} unidades, ficou R${total:.2f}!")
    print(f"\nVolte sempre!")

elif escolha == 5:
    quantidade = int(input(f"\nMuito bem! O {nome_produto5} está R${preco_produto5:.2f}"
                           f"\nQuantas unidades você vai querer: "))
    total = quantidade * preco_produto5
    print(f"\nO total da sua compra de {nome_produto5}, com {quantidade} unidades, ficou R${total:.2f}!")
    print(f"\nVolte sempre!")

else:
    print("\nCódigo de produto inválido!")


