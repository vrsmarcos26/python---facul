import mysql.connector

def create_database():
    conexao_db = mysql.connector.connect(
        user = "root",
        password = "ceub123456",
        host = "127.0.0.1")
    
    print("Conexão db: ", conexao_db)
    cursos_db = conexao_db.cursor()

    sql = "CREATE DATABASE if not exists db_loja_3"
    cursos_db.execute(sql)
    cursos_db.close()
    conexao_db.close()

def create_connection():
    con = mysql.connector.connect(
        user = "root",
        password = "ceub123456",
        host = "127.0.0.1",
        database="db_loja_3")
    print("Conexão = ", con )
    return con

def create_table():
    sql = """Create Table if not exists tb_produto(
    idt INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR (45) NOT NULL UNIQUE,
    preco DECIMAL (9,2) NOT NULL,
    dta_validade DATE NULL,
    PRIMARY KEY (idt)
    )"""

    cursor.execute(sql)

def insert():

    var1 = input("Nome: ")
    var2 = float(input("Preço: "))

    from datetime import date
    a_data = date.today()

    sql = f"""insert into tb_produto (nome, preco, dta_validade)
    values ('{var1}', '{var2}','{a_data}')"""

    cursor.execute(sql)
    conexao.commit()

def select():

    print ("Consulta")

    var1 = int(input("Consulta geral (1) ou específica (2): "))

    if var1 == 1:
        sql = """SELECT * FROM tb_produto"""
        cursor.execute(sql)
        l_registros = cursor.fetchall()
        print(l_registros)
    else:
        sql = """SELECT * FROM tb_produto WHERE nome = %s"""
        nome_param = input("Digite o nome para consulta: ")
        cursor.execute(sql, (nome_param,))
        l_registros = cursor.fetchall()
        print("- List of tuplas: ")
        print(l_registros)

def delete ():
    nome_param = input("Digite o nome para deletar: ")
    sql = f"""DELETE FROM tb_produto WHERE nome = '{nome_param}'"""
    cursor.execute(sql)
    conexao.commit()
    print("Registros apagados: ", cursor.rowcount)

def close_connection():
    cursor.close()
    conexao.close()

if __name__ == "__main__":
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()
    #insert()
    select()
    delete()
    close_connection()