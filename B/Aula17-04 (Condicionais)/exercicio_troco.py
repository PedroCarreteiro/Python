def troco():
    preco_unitario = float(input("Digite o preço unitário do produto: "))
    quantidade = int(input("Digite a quantidade de produtos: "))
    valor_cliente = float(input("Digite o valor que o cliente dado: "))

    valor_total = preco_unitario * quantidade

    if valor_cliente < valor_total:
        print(f"O valor é insuficiente, ainda faltam {valor_total-valor_cliente:.2f} reais")

    elif valor_cliente > valor_total:
        troco = valor_cliente - valor_total
        print(f"O troco é {troco:.2f} reais")

troco()

