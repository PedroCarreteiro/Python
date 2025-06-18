class Colaborador_Bosch:
    def __init__(self, nome, edv, salario, area):
        self.nome = nome
        self.__edv = edv
        self.__salario = salario
        self.area = area

    def get_nome(self):
        return self.__edv
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario_novo):
        self.__salario = salario_novo

    # def mostrar_salario(self):
    #     print(f"O salario do colaborador {self.nome} é: {self.__salario}")

    def __pedir_aumento(self, aumento):
        print(f"Quero um aumento de {aumento} reais!")
        return True

    def alteracao_salarial(self, aumento):
        resposta = self.__pedir_aumento(aumento=aumento)
        if resposta:
            print("Salário foi aumentado!")
        else:
            print("Salário continua o mesmo!")
            pass

francis_god = Colaborador_Bosch("Francis - O deus Shinobi", "92867845", "100000", "G0")

francis_god.alteracao_salarial()


# francis_salario = francis_god.get_salario()

# print(francis_salario)

# francis_god.set_salario("9999999999")

# francis_salario = francis_god.get_salario()

# print(francis_salario)

#francis_god.mostrar_salario()