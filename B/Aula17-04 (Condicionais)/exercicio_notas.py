def calculo_nota():

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    if (nota1 > 100 or nota1 < 0) or (nota2 > 100 or nota2 < 0):
        print("Notas inválidaas")

    else:

        nota_final = (nota1 + nota2) / 2

        if nota_final >= 60:
            print(f"Suas notas são: \n"
                  f"Nota 1 = {nota1:.1f}\n"
                  f"Nota 2 = {nota2:.1f}\n"
                  f"Nota final = {nota_final:.1f}\n"
                  f"Por conta de seu bom rendimento, você foi APROVADO")
        else:
            print(f"Suas notas são: \n"
                  f"Nota 1 = {nota1:.1f}\n"
                  f"Nota 2 = {nota2:.1f}\n"
                  f"Nota final = {nota_final:.1f}\n"
                  f"Por conta de seu mau rendimento, você foi REPROVADO")

calculo_nota()