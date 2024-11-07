import mysql.connector
from datetime import date

def create_database():
    conexao_db = mysql.connector.connect(user='root', password='ceub123456', host='127.0.0.1')
    print('Conexão db:', conexao_db)
    cursor_db = conexao_db.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS db_loja_3"
    cursor_db.execute(sql)
    cursor_db.close()
    conexao_db.close()
    print('\nConexão db fechada.')

def create_connection():
    con = mysql.connector.connect(user='root', password='ceub123456', host='127.0.0.1', database='db_loja_3')
    print('Conexão:', con)
    return con

def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexão fechada.')

def create_table():
    sql = """ CREATE TABLE IF NOT EXISTS tb_produto(
                idt INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(45) NOT NULL UNIQUE,
                preco DECIMAL(9,2) NOT NULL,
                dta_validade DATE NULL,
                PRIMARY KEY (idt)
              )"""
    cursor.execute(sql)

def insert():
    a_nome = input('Insert - Nome: ')
    a_preco = float(input('Preço: '))
    a_data = input('Data de validade (aaaa-mm-dd): ')
    sql = f"""INSERT INTO tb_produto (nome, preco, dta_validade) 
              VALUES ('{a_nome}', {a_preco}, '{a_data}')"""
    cursor.execute(sql)
    conexao.commit()
    print('Registros inseridos:', cursor.rowcount)

def select():
    print('- Consulta:')
    sql = 'SELECT * FROM tb_produto'
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    print('- List of tuplas:')
    print(l_registros)
    print(' - Tuplas:')
    for record in l_registros:
        print(record)
    print("- Colunas, notação de vetor:")
    for record in l_registros:
        print("- Idt:", record[0])
        print("Nome:", record[1])
        print("Preço:", record[2])
        print('Data de validade:', record[3])
    print('Quantidade de registros na tabela (rowcount):', cursor.rowcount)

def select_input():
    pesquisa = input('Digite o nome do produto para consultar: ')
    sql = f"SELECT * FROM tb_produto WHERE nome LIKE '%{pesquisa}%'"
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    if l_registros:
        for record in l_registros:
            print("- Idt:", record[0])
            print("Nome:", record[1])
            print("Preço:", record[2])
            print("Data de validade:", record[3])
    else:
        print("Nenhum registro encontrado para o critério informado.")

def delete():
    pesquisa = input('Nome do produto para excluir: ')
    sql = f"DELETE FROM tb_produto WHERE nome = '{pesquisa}'"
    cursor.execute(sql)
    conexao.commit()
    print("Registros apagados:", cursor.rowcount)

def update():
    pesquisa = input('Nome do produto que deseja alterar: ')
    novo_nome = input('Novo nome: ')
    novo_preco = float(input('Novo preço: '))
    nova_data = input('Nova data de validade (aaaa-mm-dd): ')
    sql = f"""UPDATE tb_produto 
              SET nome = '{novo_nome}', preco = {novo_preco}, dta_validade = '{nova_data}' 
              WHERE nome = '{pesquisa}'"""
    cursor.execute(sql)
    conexao.commit()
    print("Registro(s) atualizado(s):", cursor.rowcount)

def main():
    while True:
        print("\nMenu de opções:")
        print("1 - Inserir produto")
        print("2 - Consultar produtos")
        print("3 - Excluir produto")
        print("4 - Atualizar produto")
        print("5 - Sair")

        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '1':
            insert()
        elif escolha == '2':
            print("Consultar todos os produtos (1) ou consultar por nome (2)?")
            opcao = input("Escolha uma opção (1-2): ")
            if opcao == '1':
                select()
            elif opcao == '2':
                select_input()
            else:
                print("Opção inválida!")
        elif escolha == '3':
            delete()
        elif escolha == '4':
            update()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()
    main()
    close_connection()
