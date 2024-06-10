class Passaro:
    def voar(self):
        print("Estou voando")


class Pardal(Passaro):
    def voar(self):
        super().voar()


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")


class Avião(Passaro): # FIXME: Metódo errado de uso 
    def voar(self):
        print("Avião está decolando")

def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(Avião())
