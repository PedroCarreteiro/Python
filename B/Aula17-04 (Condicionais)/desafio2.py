print("==== Seja bem vindo ao sistema adivinhe a senha ====")

tentativa = True

user = input("Digite seu usuário: ")
if user == "admin":
    horario = int(input("Digite o horário atual: "))
    if horario < 18 and horario > 8 and tentativa == True:
        senha = input("Digite sua senha: ")
        if senha == "1234" and tentativa == True:
            codigo = input("Digite seu codigo de verificação: ")
            if codigo == "999" and tentativa == True:
                print("Acesso liberado!")
            else:
                print("Código incorreto!")
                print("Sistema bloqueado. Contate um adminstrador.")
                tentativa == False
        else:
            print("Senha incorreta!")
            senha = input("Digite sua senha novamente: ")
            if senha == "1234" and tentativa == True:
                codigo = input("Digite seu codigo de verificação: ")
                if codigo == "999" and tentativa == True:
                    print("Acesso liberado!")
                else:
                    print("Código incorreto!")
                    print("Sistema bloqueado. Contate um adminstrador.")
                    tentativa == False
            else:
                print("Senha incorreta!")
                print("Dica: Sua senha é composta apenas por números consecutivos.")
                senha = input("Digite sua senha novamente: ")
                if senha == "1234" and tentativa == True:
                    codigo = input("Digite seu codigo de verificação: ")
                    if codigo == "999" and tentativa == True:
                        print("Acesso liberado!")
                    else:
                        print("Código incorreto!")
                        print("Sistema bloqueado. Contate um adminstrador.")
                        tentativa == False
                else:
                    print("Sistema bloqueado. Contate um adminstrador.")
    else:
        print("Você está fazendo login fora do horário de funcionamento!")
        print("Sistema bloqueado. Contate um adminstrador.")
        tentativa == False
else:
    print("Usuário inválido!")
    print("Sistema bloqueado. Contate um adminstrador.")
    tentativa == False