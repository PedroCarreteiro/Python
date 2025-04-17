def operadora():
    valor_basico = 50
    minutos = int(input("Digite a quantidade de minutos: "))

    if minutos > 100:
        minutos_mais = minutos - 100
        taxa_minuto = minutos_mais * 2.00
        print(f"Você ficou {minutos} minutos no telefone e pagou uma taxa de {valor_basico+taxa_minuto} reais")
    else:
        print(f"Você ficou {minutos} minutos no telefone e pagou uma taxa de {valor_basico} reais")

operadora()

