nome = input("====== Seja bem vindo à Calculadora de Salários! =====\n"
             "Digite seu nome: ")

salario = float(input(f"\nOlá {nome}, esperamos que você esteja tendo um ótimo dia!\n"
                      f"Para fins de reajuste salarial, precisamos que você insira o seu salário aqui: "))

def aumento_salario(salario):
    if salario < 0:
        print("Salário invalido")
    elif salario <= 1000:
        salario_atualizado = salario + salario * 0.20
        print(
            f"\n{nome}, o seu salário foi aumentado em 20%, com um aumento total de R${salario * 0.20:.2f}, e o total de seu novo salário será R${salario_atualizado:.2f}!")
        print(f"\nObrigado por usar nossa calculadora, volte sempre!")
    elif 1000 < salario <= 3000:
        salario_atualizado = salario + salario * 0.15
        print(
            f"\n{nome},o seu salário foi aumentado em 15%, com um aumento total de R${salario * 0.15:.2f}, e o total de seu novo salário será R${salario_atualizado:.2f}!")
        print(f"\nObrigado por usar nossa calculadora, volte sempre!")
    elif 3000 < salario <= 8000:
        salario_atualizado = salario + salario * 0.10
        print(
            f"\n{nome}, o seu salário foi aumentado em 10%, com um aumento total de R${salario * 0.10:.2f}, e o total de seu novo salário será R${salario_atualizado:.2f}!")
        print(f"\nObrigado por usar nossa calculadora, volte sempre!")
    elif salario > 8000:
        salario_atualizado = salario + salario * 0.05
        print(
            f"\n{nome}, o seu salário foi aumentado em 5%, com um aumento total de R${salario * 0.05:.2f}, e o total de seu novo salário será R${salario_atualizado:.2f}!")
        print(f"\nObrigado por usar nossa calculadora, volte sempre!")

aumento_salario(salario)
