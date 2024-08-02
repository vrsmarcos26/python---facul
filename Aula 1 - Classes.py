class Veiculo(object): # Super Classe
    def __init__(self,valor,modelo,km=0): #Construtor com valor default
        self.valor = valor #Atributos de instância
        self.modelo = modelo
        self.km = km
    def get_valor(self): #Func de Consulta
        return self.valor
    def get_modelo(self):
        return self.modelo
    def get_km(self):
        return self.km
    def set_valor(self, novo_valor): #Modificar o valor
        self.valor = novo_valor
    def set_modelo(self, novo_modelo): #Modificar o valor
        self.modelo = novo_modelo
    def set_km(self, novo_km): #Modificar o valor
        self.km = novo_km        
    pass

class Carro(Veiculo):
    def __init__(self,valor,modelo,km, qtd_portas): #Construtor com valor default
        super().__init__(valor,modelo,km) #Chamando valores da classe primaria
        self.qtd_portas = qtd_portas

    def get_qts_portas(self):
        return self.qtd_portas
    def set_qtd_portas(self, nova_qtd_portas):
        self.qtd_portas = nova_qtd_portas


if __name__ == '__main__': # Func main
    v1 = Veiculo (100000.00, "Yaris", 20000)
    v2 = Veiculo (123, "gol", 999)
    print("- Veiculo 1 (alocação na memória): ", v1)
    print(f"- Valor do veiculo: {v1.get_valor()}")
    print("- Modelo do veiculo: ", v1.get_modelo())
    v1.set_valor(110000.00)
    print("- Valor alterado do veiculo", v1.get_valor())

    c1 = Carro(9000.00, "FUSCA", 1000, 4)
    print(f"\n- Carro 1: {c1}")
    print(f"\n- Quantidade de portas do carro: {c1.get_qts_portas()}")
    c1.set_qtd_portas(2)
    print("- Valor alterado da qunatidade de portas: ", c1.get_qts_portas())
    print("Valor", c1.get_valor())
    print("Modelo", c1.get_modelo())
    print("KM: ", c1.get_km())

    c2 = Carro(1000.00, "BYD", 4)
    print(f"\n- Carro 2: {c2}")
    print(f"\n- Quantidade de portas do carro: {c2.get_qts_portas()}")
    c2.set_qtd_portas(2)
    print("- Valor alterado da qunatidade de portas: ", c2.get_qts_portas())
    print("Valor", c2.get_valor())
    print("Modelo", c2.get_modelo())

    c3 = Carro(9000.00, "FUSCA")
    print(f"\n- Carro 1: {c3}")
    print(f"\n- Quantidade de portas do carro: {c3.get_qts_portas()}")
    c3.set_qtd_portas(2)
    print("- Valor alterado da qunatidade de portas: ", c3.get_qts_portas())
    print("Modelo", c3.get_modelo())



