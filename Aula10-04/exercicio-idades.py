#Inserir nomes e idade
from sys import orig_argv

nome1 = input("Pessoa 1, digite seu nome: ")
idade1 = int(input("Pessoa 1, digite sua idade: "))
nome2 = input("Pessoa 2, digite seu nome: ")
idade2 = int(input("Pessoa 2, digite sua idade: "))

#Calcular a media de idade
media_idade = (idade1 + idade2) / 2

#Mostrar resultado
print(f"Olá {nome1} e {nome2}!\n"
      f"A média de idade entre vocês é: {media_idade:.1f}")
