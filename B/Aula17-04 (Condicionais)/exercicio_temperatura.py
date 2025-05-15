nome = input("Digite seu nome: ")

conversao = input(f"\nOlá {nome}! "
                  "\n\n==== Bem vindo ao programa de transformação de temperatura! ===="
                  "\n\n========= (Digite C para Celsius ou F para Fahrenheit) ========="
                  "\n\nDigite a medida da temperatura atual aqui: ")

temperatura = float(input("\nDigite a temperatura atual: "))
conversao = conversao.upper()

if conversao == "F":
    calculo = (temperatura-32)/1.8
    print(f"\nA conversão de {temperatura} para Celsius é {calculo:.2f}!")
elif conversao == "C":
    calculo = temperatura*1.8+32
    print(f"\nA conversão de {temperatura} para Fahrenheit é {calculo:.2f}!")

else:
    print("\nValor inválido!")

print("\nObrigado e volte sempre!")

