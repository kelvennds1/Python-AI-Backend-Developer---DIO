from abc import  ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self): 
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    # pass
    def ligar(self):
        print("TV ligada")
    
    def desligar(self):
        print("TV desligada")

    @property    
    def marca(self):
        return "SAMSUNG"       
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ar condicionado ligado")
    
    def desligar(self):
        print("Ar condicionado desligado")
       
    @property        
    def marca(self):
        return "LG"
    

controle_1 = ControleTV()
controle_1.ligar()
controle_1.desligar()
print(controle_1.marca)

controle_2 = ControleArCondicionado()
controle_2.ligar()

    