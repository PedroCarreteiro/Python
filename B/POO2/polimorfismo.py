class Super:
    def __init__(self):
        pass

    def hello(self):
        print("Olá, eu sou a Super Classe")

class Sub(Super):
    def __init__(self):
        pass

    def hello(self):
        print("Olá, eu sou a Sub Classe")

class SubSub(Super):
    def __init__(self):
        pass

    def hello(self):
        print("Olá, eu sou a SubSub Classe")

teste = Super()

teste.hello()

teste2 = Sub()

teste2.hello()

teste3 = SubSub()

teste3.hello()