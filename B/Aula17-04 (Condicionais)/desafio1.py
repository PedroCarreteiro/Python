numero = int(input("==== Seja bem vindo à calculadora de palíndromo ====\n"
             "Digite um número: "))

numero = str(numero)

if numero == numero[::-1]:
    print(f"O número {numero} é um palíndromo!")
else:
    print(f"O número {numero} não é um palíndromo!")