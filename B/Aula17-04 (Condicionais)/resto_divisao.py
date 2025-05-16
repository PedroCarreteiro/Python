numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))

if numero1 % numero2 == 0:
    print(f"O número {numero1} é divisível por {numero2}")
else:
    print(f"O número {numero1} não é divisível por {numero2}")