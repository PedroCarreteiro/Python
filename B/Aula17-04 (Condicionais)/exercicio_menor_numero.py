def menor_numero():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))

    if n1 == n2 == n3:
        print(f"Os números selecionados foram todos {n1}, e o menor número é {n1}")
    elif n1 < n2 and n1 == n3:
        print(f"Os números selecionados foram {n1}, {n2}, e {n1} é o menor")
    elif n1 < n3 and n1 == n2:
        print(f"Os números selecionados foram {n1}, {n3}, e {n1} é o menor")
    elif n2 < n1 and n2 == n3:
        print(f"Os números selecionados foram {n2}, {n1}, e {n2} é o menor")
    elif n1 < n2 and n1 < n3:
        print(f"Os números selecionados foram {n1}, {n2}, {n3}, e {n1} é o menor")
    elif n2 < n1 and n2 < n3:
        print(f"Os números selecionados foram {n1}, {n2}, {n3}, e {n2} é o menor")
    elif n3 < n1 and n3 < n2:
        print(f"Os números selecionados foram {n1}, {n2}, {n3}, e {n3} é o menor")


menor_numero()