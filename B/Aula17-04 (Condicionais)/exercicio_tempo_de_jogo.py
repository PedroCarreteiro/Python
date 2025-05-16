jogo = input("==== Seja bem vindo à calculadora de tempo de jogo ====\n"
             "Digite o nome do jogo: ")

print(f"Bem vindo ao jogo {jogo}")

inicio = input("Digite a hora inicial do jogo no formato [HH:MM]: ")
fim = input("Digite a hora final do jogo no formato [HH:MM]: ")

hora_inicio = int(inicio[0:2])
minuto_inicio = int(inicio[3:])

hora_fim = int(fim[0:2])
minuto_fim = int(fim[3:])

if hora_fim <= hora_inicio:
    tempo_dia1 = 24 - hora_inicio
    tempo_dia1 = abs(tempo_dia1)
    tempo_jogo_hora = tempo_dia1+hora_fim
    if minuto_inicio > minuto_fim:
        tempo_jogo_hora = tempo_jogo_hora - 1
        tempo_jogo_minuto = (minuto_fim - minuto_inicio) + 60
    else:
        tempo_jogo_minuto = (minuto_fim - minuto_inicio)

    if (hora_inicio == hora_fim and minuto_fim > minuto_inicio) or (tempo_jogo_hora < 1):
        print("Tempo de jogo menor que 1 hora")
    elif tempo_jogo_hora >= 24 and tempo_jogo_minuto > 0:
        print(f"O jogo tem mais de 24 horas!")
    else:
        print(f"O tempo do jogo {jogo} foi de {tempo_jogo_hora} hora(s) e {tempo_jogo_minuto} minutos")
else:
    tempo_jogo_hora = hora_fim - hora_inicio
    if minuto_inicio > minuto_fim:
        tempo_jogo_hora = tempo_jogo_hora - 1
        tempo_jogo_minuto = (minuto_fim - minuto_inicio) + 60
    else:
        tempo_jogo_minuto = (minuto_fim - minuto_inicio)

    if (hora_inicio == hora_fim and minuto_fim > minuto_inicio) or (tempo_jogo_hora < 1):
        print(f"Tempo de jogo menor que 1 hora")
    elif tempo_jogo_hora >= 24 and tempo_jogo_minuto > 0:
        print(f"O jogo tem mais de 24 horas!")
    else:
        print(f"O tempo do jogo {jogo} foi de {tempo_jogo_hora} hora(s) e {tempo_jogo_minuto} minutos")