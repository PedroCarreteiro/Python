def menu():
    print("Escolha um mercado")
    print("1. Mercado São Vicente")
    print("2. Mercado Pague Menos")

    escolha = input("Digite o número do mercado desejado: ")

    if escolha == '1':
        print("Você escolheu o São Vicente")
    elif escolha == '2':
        print("Você escolheu o Pague Menos")
    else:
        print("Mercado inválido")

    if escolha == '1':
        quantidade = int(input("Digite a quantidade de items: "))
        preco_item = float(input("Digite o preço do item: "))
        preco = quantidade * preco_item
        print(f"O preço do item escolhido é de {preco_item:.2f}, e o preço total é de {preco:.2f}",end="\nObrigado pela preferência\nVolte Sempre\n")
    elif escolha == '2':
        quantidade = int(input("Digite a quantidade de items: "))
        preco_item = float(input("Digite o preço do item: "))
        preco_item *= 2
        preco = quantidade * preco_item
        print(f"O preço do item escolhido é de {preco_item:.2f}, e o preço total é de {preco:.2f}",end="\nObrigado pela preferência\nVolte Sempre\n")

menu()