from Conta_back import Titular, Conta
from abc import ABC, abstractclassmethod

if __name__ == "__main__":
    titular1 = Titular("Jubileu", 40028922, "Irineu")
    print(f"""\n ===== Titular =====
          
    - Nome {titular1.get_nome_titular()}
    - Sobrenome: {titular1.get_sobrenome_titular()}
    - Nome completo: {titular1.full_name()}
    - CPF: {titular1.get_cpf_titular()}

    """)
    titular1.set_nome_titular("Irineu")
    titular1.set_sobrenome_titular("Jubileu")
    titular1.set_cpf_titular(123456789)

    print(f"""\n ===== Titular =====
          
    - novo Nome {titular1.get_nome_titular()}
    - novo Sobrenome: {titular1.get_sobrenome_titular()}
    - novo Nome completo: {titular1.full_name()}
    - novo CPF: {titular1.get_cpf_titular()} 
    """)
    conta1 = Conta(40028, 999999, titular1, 50)
    print(f"""\n ===== Conta =====
          
    - Número da conta {conta1.get_n_conta()}
    - Saldo da conta: {conta1.get_saldo()}
    - Nome completo e CPF: {conta1.full_name()} {conta1.get_titular_cpf()}
    - Limite da conta: {conta1.get_vl_limite_conta()}

    """)