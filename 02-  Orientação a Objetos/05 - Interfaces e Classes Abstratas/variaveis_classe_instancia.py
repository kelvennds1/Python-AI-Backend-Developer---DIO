class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"Aluno: {self.nome} - {self.matricula} - {self.escola}"
    

aluno_1 = Estudante("João", "123456")
aluno_2 = Estudante("Maria", "654321")

print(aluno_1)
print(aluno_2)
print('----------------------------')

Estudante.escola = "Python"

print(aluno_1)
print(aluno_2)
print('----------------------------')

aluno_1.escola = "DIO"

print(aluno_1)
print(aluno_2)
print('----------------------------')
