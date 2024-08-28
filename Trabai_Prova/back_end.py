"""
                    CEUB - FATECS
        Bacharelado em Ciência da Computação - BCC
    Linguagem e Técnicas de Programação II - Prof. Barbosa


- Avaliação prática individual 1

- Prazo para entrega no Moodle: 29/08, até 23h59

- Envio:
Envie os arquivos na sala on-line no Moodle.


- Resolva o projeto usando a linguagem de programação Python e os conceitos de POO (Programação Orientada a Objetos), inheritance (herança) e classe abstrata (ABC).


- Implemente:

1. Crie pelo menos três classes com seus respectivos atributos e métodos. **

2. Crie uma superclasse abstrata com o construtor, pelo menos dois atributos e pelo menos um atributo com valor default. **

3. Crie todos os métodos gets e todos os métodos sets. **

4. A superclasse abstrata deve ter pelo menos um método abstrato e pelo menos dois métodos concretos. **

5. E duas subclasses concretas, os construtores, com pelo menos um atributo em cada subclasse, os métodos gets e sets. **

6. Nas duas subclasses sobrescreva o método abstrato da superclasse abstrata e pelo menos mais um método concreto. **

7. No main, crie pelo menos um objeto de cada classe e use (teste) todos os métodos implementados das três classes. **

Obs.: crie as classes e os métodos diferentes dos desenvolvidos nas aulas.


"""

from abc import ABC, abstractmethod
import random

class Heroi(ABC):   #Superclasse Abstrata
    def __init__(self, nome ,genero, raça, idade=0, vida=0, carisma=0):
        self.nome = nome
        self.vida = vida
        self.genero = genero
        self.raça = raça
        self.idade = idade
        self.carisma = carisma
    
    def get_vida (self):                #Métodos Gets/Sets
        return self.vida
    def set_vida (self, nova_vida):
        self.vida = nova_vida
        return
    
    def get_nome (self):
        return self.nome
    def set_nome (self, nova_nome):
        self.nome = nova_nome
        return
    
    def get_genero (self):
        return self.genero
    def set_genero (self, nova_genero):
        self.genero = nova_genero
        return
    
    def get_raça (self):
        return self.raça
    def set_raça (self, nova_raça):
        self.raça = nova_raça
        return
    
    def get_idade (self):
        return self.idade
    def set_idade (self, nova_idade):
        self.idade = nova_idade
        return
    
    def get_carisma (self):    #Método concreto 1
        if self.carisma <= 4:
            return "Personalidade fraca"
        elif self.carisma <= 6:
            return "Personalidade média"
        else:
            return "Personalidade boa"
    
    def set_carisma (self, nova_carisma):
        self.carisma = nova_carisma
        return
    
    @abstractmethod             #Metódo abstrato
    def usar_habilidade(self):
        ...

    def Obj_iniciais (self):    #Método concreto 2
        lista_de_obj = ['Espada', 'banana', 'cereja', 'arco', 'cajado', 'adaga','pedra','coco de cavalo', 'pote de aguá', 'chicote']
        objts_aleatorias = [random.choice(lista_de_obj) for _ in range(3)]
        return objts_aleatorias

    
    
    def __str__(self):
        return f"Eu sou um herói! Nome: {self.nome}, Vida: {self.vida}, Gênero: {self.genero}, Idade: {self.idade}, Raça: {self.raça}, Carisma {self.carisma}, "


class Mago(Heroi):
    def __init__(self, nome, genero, raça, magia, idade=0, vida=0,carisma=0,mana=0):
        super().__init__(nome, genero, raça, idade, vida*random.randint(1, 10), carisma)
        self.mana = mana
        self.magia = magia

    def get_magia (self):
        return self.magia
    def set_magia (self, nova_magia):
        self.magia = nova_magia
        return
    
    def get_mana (self):
        return self.mana + random.randint(1, 5)
    def set_mana (self, nova_mana):
        self.mana = nova_mana
        return
    
    def Elemento(self): #Método concreto 1
        lista_de_obj = ['Fogo', 'Água', 'Vento','Planta' ]
        objts_aleatorias = random.choice(lista_de_obj)
        return objts_aleatorias
    
    def usar_habilidade(self):
        return f"O mago está usando a magia de {self.magia}!"

    def apresentar(self):
        return super().__str__() + f" Magia: {self.magia}, Mana: {self.mana}"
    
class Ladino(Heroi):
    def __init__(self, nome, genero, raça, tecnica, idade=0, vida=0, carisma=0, furtividade=0):
        super().__init__(nome, genero, raça, idade, vida*random.randint(1, 10), carisma)
        self.furtividade = furtividade
        self.tecnica = tecnica

    def get_tecnica (self):
        return self.tecnica
    def set_tecnica (self, nova_tecnica):
        self.tecnica = nova_tecnica
        return
    
    def get_furtividade (self):
        return self.furtividade + random.randint(1, 6)
    def set_furtividade(self, nova_furtividade):
        self.furtividade = nova_furtividade
        return
    
    def Elemento(self): #Método concreto 1
        lista_de_obj = ['Assassino', 'Mago', 'Ladrão' ]
        objts_aleatorias = random.choice(lista_de_obj)
        return objts_aleatorias
    
    def usar_habilidade(self):
        return f"O Ladino está usando a tecnica {self.tecnica}!"
    
    def apresentar(self):
        return super().__str__() + f" Tecnica: {self.tecnica}, Furtividade: {self.furtividade}"
    
class Guerreiro(Heroi):
    def __init__(self, nome, genero, raça, golpe, idade=0, vida=0, carisma=0, fúria=0):
        super().__init__(nome, genero, raça, idade, vida*random.randint(1, 10),carisma)
        self.fúria = fúria
        self.golpe = golpe

    def get_fúria (self):
        return self.fúria + random.randint(1, 8)
    def set_fúria (self, nova_fúria):
        self.fúria = nova_fúria
        return
    
    def get_golpe (self):
        return self.golpe
    def set_golpe (self, nova_golpe):
        self.golpe = nova_golpe
        return
    
    def Elemento(self): #Método concreto 1
        lista_de_obj = ['Tank', 'Lutador', 'Guerreiro']
        objts_aleatorias = random.choice(lista_de_obj)
        return objts_aleatorias
    
    def usar_habilidade(self):
        return f"O Guerreiro está usando o golpe {self.golpe}!"
    
    def apresentar(self):
        return super().__str__() + f" Golpe: {self.golpe}, fúria: {self.fúria}"

    