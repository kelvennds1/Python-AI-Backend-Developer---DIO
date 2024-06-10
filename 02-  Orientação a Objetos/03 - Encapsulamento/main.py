class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo
        self._limite = limite
    
    def depositar(self, valor):
        #...
        self._saldo += valor
    
    def sacar(self, valor):
        #...
        self._saldo -= valor

    def mostrar_saldo(self):
        #...
        return self._saldo
    


conta = Conta("0001", "João", 100, 1000)
conta.depositar(50)
print(conta.numero)
print(conta.mostrar_saldo())