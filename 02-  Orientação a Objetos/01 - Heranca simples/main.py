# %% 
class Veiculo:
    def __init__(self,cor,placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):   # Método
        print("Motor ligado")

    def desligar_motor(self):
        print("Motor desligado")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"

class Motoclicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self,):
        print(f"O caminhão {'não ' if not self.carregado else ''}está carregado")


moto = Motoclicleta("Azul","ABC-123",2)
moto.ligar_motor()

carro = Carro("Prata","DEF-456",4)
carro.ligar_motor()

caminhao = Caminhao("Vermelho","GHI-789",6, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
