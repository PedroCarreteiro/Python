#Inserção de valores
a = float(input("Digite a medida de A: "))
b = float(input("Digite a medida de B: "))
c = float(input("Digite a medida de C: "))

#Cálculo de areas
area_quadrado = a**2
area_triangulo = (a * b) / 2
area_trapezio = ( ( a + b ) * c ) / 2

#Imprimir resultados
print(f"A área do quadrado é {area_quadrado:.4f}\n"
      f"A área do triângulo retângulo é {area_triangulo:.4f}\n"
      f"A área do trapézio é {area_trapezio:.4f}")