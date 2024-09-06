from abc import ABC, abstractclassmethod

class Titular(object):
    def __init__(self,nome_titular,cpf_titular,sobrenome_titular="") -> None:
        self.nome_titular = nome_titular
        self.sobrenome_titular = sobrenome_titular
        self.cpf_titular = cpf_titular

    def get_nome_titular(self):
        return self.nome_titular
    
    def get_sobrenome_titular(self):
        return self.sobrenome_titular
    
    def get_cpf_titular(self):
        return self.cpf_titular
    
    def set_nome_titular(self, novo_nome_titular):
        self.nome_titular = novo_nome_titular

    def set_sobrenome_titular(self,novo_sobrenome_titular):
        self.sobrenome_titular = novo_sobrenome_titular

    def set_cpf_titular(self, novo_cpf_titular):
        self.cpf_titular = novo_cpf_titular

    def full_name(self):
        full_name = f"{self.nome_titular} {self.sobrenome_titular}"
        return full_name
    
    def __str__(self):
        return f"Nome completo {self.nome_titular} {self.sobrenome_titular}. CPF: {self.cpf_titular} "

class Conta(object):
    def __init__(self,n_conta,saldo_conta, o_titular, vl_limite_conta=100.00):
        self.n_conta = n_conta
        self.titular = o_titular
        self.saldo_conta = saldo_conta
        self.vl_limite_conta = vl_limite_conta

    def get_saldo(self):
        return self.saldo_conta
    def get_titular (self):
        return self.titular
    def get_titular_nome(self):
        return self.titular.get_nome_titular()
    def get_titular_sobrenome(self):
        return self.titular.get_sobrenome_titular()
    def full_name(self):
        return self.titular.full_name()
    def get_titular_cpf(self):
        return self.titular.get_cpf_titular()
    def get_n_conta (self):
        return self.n_conta
    def get_vl_limite_conta (self):
        return self.vl_limite_conta
    
    def set_saldo_conta (self,novo_saldo_conta):
        self.saldo_conta = novo_saldo_conta

    def set_n_conta (self,novo_n_conta):
        self.n_conta = novo_n_conta

    def set_vl_limite_conta (self,novo_vl_limite_conta):
        self.vl_limite_conta = novo_vl_limite_conta

    def __str__(self):
        super_str = super().__str__()
        return f"{self.n_conta}, {self.titular}, {self.saldo_conta}, {self.vl_limite_conta}"

    


