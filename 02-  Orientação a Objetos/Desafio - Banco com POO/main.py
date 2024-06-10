from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty
from datetime import datetime

class Cliente():
    def __init__(self, endereco: str):
        self.endereco: str = endereco
        self.contas: list[str] = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str ):
        super().__init__(endereco)
        self.nome: str = nome
        self.data_nascimento: str = data_nascimento
        self.cpf: str = cpf 
        
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente,):        
        return cls(cls.proxima_numero(), cliente)
    
    @staticmethod
    def proxima_numero():
        return Conta.numero_total() + 1
    
    @staticmethod
    def numero_total():
        return Conta.total_contas()
    
    @staticmethod
    def total_contas():
        return len(Conta.contas)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo_atual = self._saldo
        excedeu_saldo = valor > saldo_atual
        
        if excedeu_saldo:
            print("Saldo insuficiente")

        elif valor > 0:
            self._saldo -= valor 
            print("\nSaque realizado com sucesso!")
            return True
        
        else:
            print("Valor inválido")
            
        return False
    
    def depositar (self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso!")
            return True
        
        else:
            print("Valor inválido")
            
        return False
    
    def extrato(self):
        print(f"Ag/Cc: {self._agencia}/{self._numero}")
        print(f"Saldo: {self._saldo}")
        print(f"Cliente: {self._cliente.nome}")
        print(f"CPF: {self._cliente.cpf}")
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saque
        
        if excedeu_limite or excedeu_saques:
            print("Operação negada!")
            
        elif valor > 0:
            return super().sacar(valor)
                    
        return False
    
    def __str__(self) -> str:
        return f"""\
            Agencia:\t{self._agencia}
            Numero:\t{self._numero}
            Titular:\t{self._cliente.nome}
        """
        
class Historio:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': str(transacao.__class__.__name__),
                'valor': transacao.valor,
                'data': datetime.now().strftime
                ('%d/%m/%Y %H:%M:%S'),
            }
        )
        
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)
        return conta.sacar(self.valor)
    
    def __str__(self) -> str:
        return f"Saque: {self.valor}"

class Deposito(Transacao):
    
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)
        return conta.depositar(self.valor)
    
    def __str__(self) -> str:
        return f"Depósito: {self.valor}"
    
    