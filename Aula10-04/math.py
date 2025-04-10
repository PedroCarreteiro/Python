import math

#Solicitar um número ao usuario
numero = float(input("Digite um número para calcular a raiz quadrada: "))

#Calcular a raiz quadrada da variável numero
raiz_quadrada = math.sqrt(numero)

#Exibir resultado
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")