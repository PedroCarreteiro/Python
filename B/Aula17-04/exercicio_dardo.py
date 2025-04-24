lancamento1 = float(input("Digite a distância do primeiro lançamento: "))
lancamento2 = float(input("Digite a distância do segundo lançamento: "))
lancamento3 = float(input("Digite a distância do terceiro lançamento: "))

if lancamento1 > lancamento2 and lancamento1 > lancamento3:
    print(f"O primeiro lançamento foi o maior, com uma distância de: {lancamento1}")
elif lancamento2 > lancamento1 and lancamento2 > lancamento3:
    print(f"O segundo lançamento foi o maior, com uma distância de: {lancamento2}")
elif lancamento3 > lancamento1 and lancamento3 > lancamento2:
    print(f"O terceiro lançamento foi o maior, com uma distância de: {lancamento3}")