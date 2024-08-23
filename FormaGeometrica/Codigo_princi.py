from abc import ABC, abstractmethod #importa o módulo ABC (Abstract base ckasses)

class FormaGeometrica(ABC):         #Classe abstrata, herda da classe ABC
    def __init__(self):
        ... #pass
        #Método abstrato, obrigatório pelo menos um na superclasse abstrata
        @abstractmethod
        def area(self):             #Método abstrato
            ...                     #Equivalente: pass
        
        @abstractmethod             #Decorator
        def perimetro(self):        #Método abstrato
            pass                    #Equivalente: ...

class Quadrado(FormaGeometrica):
    def __init__(self,lado):
        super().__init__()
        self.lado = lado

    def get_lado(self):
        return self.lado
    def set_lado(self,novo_lado):
        self.lado = novo_lado
    def area(self):
        vl_area = self.lado ** 2
        return vl_area
    def perimetro(self):
        vl_perimetro = self.lado * 4
        return vl_perimetro

class Circulo(FormaGeometrica):
    def __init__(self,raio):
        super().__init__()
        self.raio = raio
    
    def get_raio(self):
        return self.raio
    def set_raio(self,novo_raio):
        self.raio = novo_raio
        return novo_raio
    def area_qd(self):
        vl_area_qd = 3.14 * (self.raio ** 2)
        return vl_area_qd
    
    