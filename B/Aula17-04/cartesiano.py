x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

if x == 0 and y == 0:
    print("A coordenada está na origem")
elif x == 0 and (y>0 or y<0):
    print("A coordenada está no eixo Y")
elif (x>0 or x<0) and y == 0:
    print("A coordenada está no eixo X")
elif x>0 and y>0:
    print("A coordenada está no quadrante Q1")
elif x<0 and y>0:
    print("A coordenada está no quadrante Q2")
elif x<0 and y<0:
    print("A coordenada está no quadrante Q3")
elif x>0 and y<0:
    print("A coordenada está no quadrante Q4")