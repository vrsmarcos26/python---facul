"""                 Comentários de várias linhas

  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Com base nos conceitos de POO (Programação Orientada a Objetos) e
inheritance (herança), implemente a entidade veículo com as
especializações de carro e moto.

- Precisamos trabalhar com as características (atributos):
valor, modelo, quilometragem, quantidade de portas e cilindradas.

- Levante as características comuns e as características específicas de
um carro e de uma moto.

- Implementados na aula:

1- Crie a superclasse Veiculo e o construtor (__init__) com os atributos comuns:
   valor, modelo (Corolla, Argo etc.) e km que indica a quilometragem.
   Use pelo menos um atributo default (padrão). No main, teste FEITO
2- Crie os métodos gets e sets da superclasse. FEITO
3- Antes do método main, crie a subclasse Carro, que herda da superclasse Veiculo. O
   construtor com os atributos valor, modelo, km e qtd_portas. E os métodos get e set. FEITO
4- Crie três instâncias da subclasse Carro com quatro, três e dois argumentos.
   No main, teste FEITO

- Implementar para o próxima aula:

5- Na subclasse Carro, sobrescreva o método __str__ do Python, ele retorna todos os
   dados (atributos). No main, teste FEITO
6- Antes do método main, crie a subclasse Moto, que herda a superclasse Veiculo. O
   construtor com os três atributos comuns e o atributo cilindradas. E os métodos get e set FEITO
7- Crie duas instâncias (objetos) da classe Moto com quatro e três argumentos.
   Teste FEITO
8- Utilizr o método vars() para acessar os atributos de Carro e Moto num dicionário.
    Sintaxe: print(vars(objeto))
9- Use o método  __dict__ para acessar os atributos de Carro e Moto num dicionário.
    Sintaxe: print(objeto.__dict__)
10- Método de acrescentar
11- Método de condição


"""

# Nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class Veiculo:            # Três formas equivalentes de criar classe
# class Veiculo():
class Veiculo(object):  # Superclasse
    def __init__(self, valor, modelo, km=0):  # Construtor com valor default
        self.valor = valor  # Atributos de instância
        self.modelo = modelo
        self.km = km
    def get_valor(self):                      # Consulta
        return self.valor
    def set_valor(self, novo_valor):          # Sem crítica
        self.valor = novo_valor
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    def get_km(self):
        return self.km
    def set_km(self, nova_km):
        self.km = nova_km
    def acrescentar_valor(self,add_valor):
        self.valor = self.valor + add_valor
        return self.valor
    def condição(self):
        if self.km == 0:
            return "Vaiculo NOVO"
        elif self.km > 0 & self.km <= 2000:
            return "Veiculo semi-novo"
        else:
            return "Veiculo usado"

    def __str__(self):
        return f'Veículo (valor= {self.valor}, modelo = {self.modelo}, km= {self.km})'
    


# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class NomeSubclasse(NomeSuperclasse):   # Sintaxe
class Carro(Veiculo):       # A subclasse Carro herda da superclasse Veiculo
    def __init__(self, valor, modelo, km=0, qtd_portas=4):  # Valor default
        super().__init__(valor, modelo, km)  # Chama construtor da superclasse
        self.qtd_portas = qtd_portas
    def get_qtd_portas(self):
        return self.qtd_portas
    def set_qtd_portas(self, nova_qtd):
        self.qtd_portas = nova_qtd
    def __str__(self):
        # Chama o __str__ da superclasse e adiciona a informação da subclasse
        super_str = super().__str__()
        return f'{super_str}, qtd_portas = {self.qtd_portas}'


class Moto(Veiculo):
    def __init__ (self, valor, modelo, km=0, cilindradas=0):
        super().__init__(valor,modelo,km)
        self.cilindradas = cilindradas
    def get_cilindrada(self):
        return self.cilindradas
    def set_cilindrada(self,nova_cilindrada):
        self.cilindradas = nova_cilindrada
    def __str__ (self):
        super_str = super().__str__()
        return f'{super_str}, cilindrada = {self.cilindradas}'

if __name__ == '__main__':                      # Atalho: main
    v1 = Veiculo (100000.00, "Yaris", 20000)
    print("- Veiculo 1:", v1)
    print(f'Valor: {v1.get_valor()}')
    print('Modelo:', v1.get_modelo())
    v1.set_valor(110000.00)
    print(f'Valor alterado: {v1.get_valor()} \n')
    

    c1 = Carro(99000.00, "Civic", 1000, 4)  # Instancia objeto da subclasse
    print('- Carro 1:\n', c1)               # print(c1.__str__())
    
    print(f'Valor: {c1.get_valor():.2f}')   # Duas casas decimais
    print('Modelo:', c1.get_modelo())
    print(f'Qtd. portas, {c1.get_qtd_portas()} \n')

    
    c2 = Carro(100000.00, 'Corolla', 5000)  # Três argumentos
    print('- Carro 2:\n', c2)
    print(f'Valor: {c2.get_valor():.2f}')
    print('Modelo:', c2.get_modelo())
    print('Km:', c2.get_km())
    print(f'Qtd. portas, {c2.get_qtd_portas()}\n')

    c3 = Carro(70000.00, 'HB20')            # Dois argumentos
    print('- Carro 3:\n', c3)
    print(f'Valor: {c3.get_valor():.2f}')
    print('Modelo:', c3.get_modelo())
    print('Km:', c3.get_km())
    print('Qtd. portas', c3.get_qtd_portas())
    c3.set_valor(88000.00)
    print(f'Preço alterado: {c3.get_valor():.2f} \n')

    m1 = Moto(5000.00, 'Ninja', 400, 350)    # Quadro argumentos
    print(f"- Moto 1:\n {m1}")
    print(f"Valor: {m1.get_valor()}")
    print(f"Modelo: {m1.get_modelo()}")
    print(f"Km: {m1.get_km()}")
    print(f"Cilindrada: {m1.get_cilindrada}")
    m1.set_cilindrada(400.00)
    print(f"Cilindrada alterada: {m1.get_cilindrada()}")

    m2 = Moto(4000.00, "Harley", 300)         # Três argumentos
    print(f"- Moto 2:\n {m2}")
    print(f"- Valor: {m2.get_valor()}")
    m2.acrescentar_valor(360.00)
    print(f"- Novo Valor: {m2.get_valor()}")
    print(f"- Modelo: {m2.get_modelo()}")
    print(f"- KM: {m2.get_km()}")
    print(m2.condição())
    m2.set_km(200)
    print(f"Km alterado: {m2.get_km()}")
    print(m2.__dict__)
    print(vars(m2))
    
