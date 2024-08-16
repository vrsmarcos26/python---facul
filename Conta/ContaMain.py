from ContaPrin import Conta
from ContaPrin import Pessoa_Fisica
from ContaPrin import Pessoa_Juri

if __name__ == '__main__':
    c = Conta("Alice", 1997.00)
    print(f"""------- Conta ------
          
    Nome do dono da Conta: {c.get_nome()}
    Valor da conta: {c.get_saldo()}
    {c.deposito(3.00)}
    Após fazer um deposito, ficou com {c.get_saldo()}
    {c.retirada(3.00)} 
    Após fazer um saque, ficou com {c.get_saldo()}
    Após tentar fazer saque maior que seu saldo: {c.retirada(3000.00)}
    
    Resolução Final: {c}

    Método vars: {vars(c)}
""")
    
    c.set_nome("Marcos")
    c.set_saldo(99999.99)

    print(f"""------- Conta ------
          
    Nome do dono da Conta: {c.get_nome()}
    Valor da conta: {c.get_saldo()}
    
    Resolução Final: {c}

    Método vars: {vars(c)}
""")


    pj = Pessoa_Juri("Catharina", 200.00, "Empresa Tec" ,"987.987.897-09")
    print(f""" ------- Conta Pessoa Juri ------
          
    Nome da pessoa JURÍDICA: {pj.get_nome()}
    Valor da conta: {pj.get_saldo()}
    Modalidade: {pj.get_modalidade()}
    CNPJ da conta: {pj.get_cnpj()}

    Resolução Final: {pj}

    Método vars: {vars(pj)}
""")
    
    pj.set_nome("Miguel")
    pj.set_saldo(300.00)
    pj.set_modalidade("Empresa de CyberSecuity")
    pj.set_cnpj("123.456.789-0")

    print(f""" ------- Conta Pessoa Juri ------
          
    Nome da pessoa JURÍDICA: {pj.get_nome()}
    Valor da conta: {pj.get_saldo()}
    Modalidade: {pj.get_modalidade()}
    CNPJ da conta: {pj.get_cnpj()}

    Resolução Final: {pj}

    Método vars: {vars(pj)}

""")

    pf = Pessoa_Fisica("Edu", 4000.00, "Masculino","400.289.220-12")
    print(f""" ------- Conta Pessoa Fisica ------
          
    Nome da pessoa JURÍDICA: {pf.get_nome()}
    Valor da conta: {pf.get_saldo()}
    Genero da pessoa: {pf.get_genero()}
    CNPJ da conta: {pf.get_cpf()}

    Resolução Final: {pf}

    Método vars: {vars(pf)}
""")
    
    pf.set_nome("Gabi")
    pf.set_saldo(5000.00)
    pf.set_genero("Feminino")
    pf.set_cpf("978.654.321-98")

    print(f""" ------- Conta Pessoa Fisica ------
          
    Nome da pessoa JURÍDICA: {pf.get_nome()}
    Valor da conta: {pf.get_saldo()}
    Genero da pessoa: {pf.get_genero()}
    CNPJ da conta: {pf.get_cpf()}

    Resolução Final: {pf}
    
    Método vars: {vars(pf)}
""")
    
