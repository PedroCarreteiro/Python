#Importar biblioteca math
import math

#Inserção de valores do retêngulo
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

#Calcular a área
area = base * altura

#Calcular prerímetro
perimetro = (base*2) + (altura*2)

#Calcular diagonal
diagonal = base**2 + altura**2
diagonal_final = math.sqrt(diagonal)

#Imprimir resultados
print(f"A área é {area:.4f}")
print(f"O perímetro é {perimetro:.4f}")
print(f"A diagonal é {diagonal_final:.4f}")