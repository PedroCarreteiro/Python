#Inserção de valores
distancia = float(input("Digite a distância total percorrida: "))
combustivel = float(input("Digite o total de combustível gasto: "))

#Calculo do consumo
consumo = distancia / combustivel

#Imprimir valores
print(f"O consumo do carro por km é {consumo:.3f} litros por km")