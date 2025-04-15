#Inserção de valores
preco_unitario = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade de produtos: "))
valor_cliente = float(input("Digite o valor do cliente: "))

#Cálulo de total
preco_total = preco_unitario * quantidade

#Cálculo de troco
troco = valor_cliente-preco_total

#Imprimir resultado
print(f"O valor do troco a ser devolvido ao cliente é: {troco}")