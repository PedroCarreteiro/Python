import math

def baskara():
    import math
    a = float(input("Digite o coeficiente de a: "))
    b = float(input("Digite o coeficiente de b: "))
    c = float(input("Digite o coeficiente de c: "))

    delta = b**2 - (4 * a * c)

    if delta >= 0:
        #if math.sqrt(delta) % 1 == 0:

        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)

        print(f"O x1 é {x1:.4f}")
        print(f"O x2 é {x2:.4f}")

        # else:
        #     print("Os valores não formam uma raíz real!")

    else:
        print("Os valores não formam uma raíz real!")

baskara()