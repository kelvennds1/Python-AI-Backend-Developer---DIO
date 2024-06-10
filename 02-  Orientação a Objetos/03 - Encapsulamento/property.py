class Foo:
    def __init__(self, x=None):
        self._x = x
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be non-negative")
        self._x = value
        
    @x.deleter
    def x(self):
        del self._x

# Testando o encapsulamento
f = Foo(5)
print(f.x)  # Saída: 5

f.x = 10
print(f.x)  # Saída: 10

# f.x = -1  # Gera uma exceção ValueError

del f.x  # Gera uma exceção AttributeError

# Acessando o atributo privado
print(f._x)  # Acesso não recomendado, pois pode levar a confusão

# Modificando o atributo privado
f._x = 15
print(f.x)  # Saída: 15

# Acessando o atributo protegido
