glicose = float(input("Digite sua glicose: "))

classificacao = ""

if glicose <= 100:
    classificacao = "Normal"
elif 140 >= glicose > 100:
    classificacao = "Elevado"
elif glicose > 140:
    classificacao = "Diabetes"

print(f"Sua classificação é: {classificacao}")