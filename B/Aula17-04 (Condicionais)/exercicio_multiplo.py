nome = input("==== Seja bem vindo à calculadora de múltiplos! ====\n"
             "Digite o seu nome: ")

print(f"== Olá {nome}! ==")
n1 = int(input(f"{nome}, digite o primeiro número: "))
n2 = int(input(f"{nome}, digite o segundo número: "))

if n1 > 0 and n2 > 0:
    if n1 > n2:
        if n1 % n2 == 0:
            print(f"O número {n1} é múltiplo de {n2}!")
        else:
            print(f"O número {n1} não é múltiplo de {n2}")
    elif n2 > n1:
        if n2 % n1 == 0:
            print(f"O número {n2} é múltiplo de {n1}")
        else:
            print(f"O número {n2} não é múltiplo de {n1}")
    else:
        print("Os números são iguais!")
else:
    print("Números inválidos!")

print("\nMuito obrigado por utilizar nossa calculadora!\n")
print("==== Volte sempre! ====")