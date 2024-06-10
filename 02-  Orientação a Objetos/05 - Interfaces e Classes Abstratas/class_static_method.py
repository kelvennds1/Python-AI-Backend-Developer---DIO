import datetime


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_pessoa_pela_data_nascimento(cls, nome, ano, mes, dia):
        idade = datetime.datetime.now().year - ano
        return cls(nome, idade)
    
    @staticmethod 
    def eh_maior_idade(idade):
        return idade >= 18
    
class Carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor

    @classmethod
    def criar_carro_pela_marca_e_ano(cls, marca, ano):
        return cls(marca, ano)
    
    
p1 = Pessoa.criar_pessoa_pela_data_nascimento('João', 1990, 1, 1)
print(p1.nome, p1.idade)

print(Pessoa.eh_maior_idade(18))
print(Pessoa.eh_maior_idade(17))

