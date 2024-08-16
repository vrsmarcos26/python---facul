class Conta(object):
    def __init__(self,nome,saldo=0):
        self.nome = nome
        self.saldo = saldo
    def get_nome(self):
        return self.nome
    def get_saldo(self):
        return self.saldo
    def set_nome(self,novo_nome):
        self.nome = novo_nome
    def set_saldo(self,novo_saldo):
        self.saldo = novo_saldo
    def deposito(self, valor):
        self.saldo += valor
    def retirada(self,valor):
        if valor > self.saldo:
            print("Transação não autorizada")
        else:
            self.saldo -= valor
        
    def __str__(self):
        return f"Nome = {self.nome} , Saldo = {self.saldo}"

class Pessoa_Juri(Conta):
    def __init__(self, nome, saldo=0, modalidade="", cnpj=""):
        super().__init__(nome, saldo)
        self.modalidade = modalidade
        self.cnpj = cnpj

    def get_modalidade(self):
        return self.modalidade
    
    def set_modalidade(self, nova_modalidade):
        self.modalidade = nova_modalidade

    def get_cnpj(self):
        return self.cnpj
    
    def set_cnpj(self, novo_cnpj):
        self.cnpj = novo_cnpj

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}, CNPJ = {self.cnpj}"

class Pessoa_Fisica(Conta):
    def __init__(self, nome, saldo=0, genero="", cpf=""):
        super().__init__(nome, saldo)
        self.genero = genero
        self.cpf = cpf

    def get_genero(self):
        return self.genero
    
    def set_genero(self, novo_genero):
        self.genero = novo_genero

    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    
    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}, genero = {self.genero},CPF = {self.cpf}"
