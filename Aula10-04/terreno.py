#Solicitar mediadas
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))

#Solicitar valor do metro quadrado
valor = float(input("Digite o valor do metro quadrado: "))

#Calcular tamanho do terreno
area = largura * comprimento

#Calcular valor do terreno
preco = area * valor

#Saída
print(f"O terreno de {area:.2f} tem o preço de {preco:.2f}")