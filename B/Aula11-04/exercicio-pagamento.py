#Inserção de valores
nome = input("Digite o nome do funcionário: ")
valor = float(input("Qual o valor que ele recebe por hora: "))
horas = float(input("Digite a quantidade de horas trabalhadas: "))

#Calculo de pagamento
pagamento = valor * horas

#Imprimir resultado
print(f"O salário do colaborador {nome} é {pagamento:.2f}")