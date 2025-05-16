print("==== Bem vindo ao programa de cadastro de usuário! ====")

nome_user1 = input("Usuário1, digite seu nome: ")
senha_user1 = input("Usuário1, digite sua senha: ")
resposta_user1 = input("Usuário1, qual o nome do seu pet: ")
print(f"Usuário {nome_user1} cadastrado!")

nome_user2 = input("Usuário2, digite seu nome: ")
senha_user2 = input("Usuário2, digite sua senha: ")
resposta_user2 = input("Usuário2, qual o nome do seu pet: ")
print(f"Usuário {nome_user2} cadastrado!")

nome_user3 = input("Usuário3, digite seu nome: ")
senha_user3 = input("Usuário3, digite sua senha: ")
resposta_user3 = input("Usuário3, qual o nome do seu pet: ")
print(f"Usuário {nome_user3} cadastrado!")

opcao = int(input("1 - Digitar senha\n"
              "2 - Recuperar senha\n"
              "3 - Sair do programa\n"
              "Qual opção você deseja realizar: "))

if opcao == 1:
    user = input("Digite o usuário: ")
    if user == nome_user1:
        senha = input(f"Olá {nome_user1} digite sua senha (Tentativa 1 de 3): ")
        if senha == senha_user1:
            print(f"Bem vindo {nome_user1}!")
        else:
            senha = input(f"Senha incorreta! {nome_user1} digite sua senha (Tentativa 2 de 3): ")
            if senha == senha_user1:
                print(f"Bem vindo {nome_user1}!")
            else:
                senha = input(f"Senha incorreta! {nome_user1} digite sua senha (Tentativa 3 de 3): ")
                if senha == senha_user1:
                    print(f"Bem vindo {nome_user1}!")
                else:
                    print("Tentativas esgotadas, acesso bloqueado!")

    elif user == nome_user2:
        senha = input(f"Olá {nome_user2} digite sua senha (Tentativa 1 de 3): ")
        if senha == senha_user2:
            print(f"Bem vindo {nome_user2}!")
        else:
            senha = input(f"Senha incorreta! {nome_user2} digite sua senha (Tentativa 2 de 3): ")
            if senha == senha_user2:
                print(f"Bem vindo {nome_user2}!")
            else:
                senha = input(f"Senha incorreta! {nome_user2} digite sua senha (Tentativa 3 de 3): ")
                if senha == senha_user2:
                    print(f"Bem vindo {nome_user2}!")
                else:
                    print("Tentativas esgotadas, acesso bloqueado!")

    elif user == nome_user3:
        senha = input(f"Olá {nome_user3} digite sua senha (Tentativa 1 de 3): ")
        if senha == senha_user3:
            print(f"Bem vindo {nome_user3}!")
        else:
            senha = input(f"Senha incorreta! {nome_user3} digite sua senha (Tentativa 2 de 3): ")
            if senha == senha_user3:
                print(f"Bem vindo {nome_user3}!")
            else:
                senha = input(f"Senha incorreta! {nome_user3} digite sua senha (Tentativa 3 de 3): ")
                if senha == senha_user3:
                    print(f"Bem vindo {nome_user3}!")
                else:
                    print("Tentativas esgotadas, acesso bloqueado!")
    else:
        print("Usuário não encontrado!")

elif opcao == 2:
    user = input("Digite o seu usuário: ")
    if user == nome_user1:
        pergunta = input(f"Olá {nome_user1}. Qual o nome do seu pet: ")
        if pergunta == resposta_user1:
            print(f"Olá {nome_user1}. Sua senha é {senha_user1}")
        else:
            print("Resposta incorreta, acesso bloqueado!")
    elif user == nome_user2:
        pergunta = input(f"Olá {nome_user2}. Qual o nome do seu pet: ")
        if pergunta == resposta_user2:
            print(f"Olá {nome_user2}. Sua senha é {senha_user2}")
        else:
            print("Resposta incorreta, acesso bloqueado!")
    elif user == nome_user3:
        pergunta = input(f"Olá {nome_user3}. Qual o nome do seu pet: ")
        if pergunta == resposta_user3:
            print(f"Olá {nome_user3}. Sua senha é {senha_user3}")
        else:
            print("Resposta incorreta, acesso bloqueado!")
    else:
        print("Usuário não encontrado!")

elif opcao == 3:
    print("Você saiu do sistema!")

else:
    print("Opção não encontrada, você foi desconectado do sistema!")