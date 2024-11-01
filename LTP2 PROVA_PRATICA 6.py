import mysql.connector

def criar_banco_e_tabela():
    # Conectar ao MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='vrsmarcos26',
        password='12345', 
    )

    cursor = connection.cursor()

    # Criar a base de dados
    cursor.execute("CREATE DATABASE IF NOT EXISTS ExemploDB")
    cursor.execute("USE ExemploDB")

    # Criar a tabela
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produtos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        codigo VARCHAR(50) NOT NULL UNIQUE,
        preco DECIMAL(10, 2) NOT NULL,
        data_validade DATE,
        descricao VARCHAR(255)
    )
    """)

    # Fechar a conexão
    cursor.close()
    connection.close()

def inserir_dados():
    connection = mysql.connector.connect(
        host='localhost',
        user='vrsmarcos26',
        password='12345', 
        database='ExemploDB'
    )

    cursor = connection.cursor()

    # Inserir dados
    for _ in range(5):
        nome = input("Digite o nome do produto: ")
        codigo = input("Digite o código do produto (único): ")
        preco = float(input("Digite o preço do produto: "))
        data_validade = input("Digite a data de validade (YYYY-MM-DD): ")
        descricao = input("Digite uma descrição do produto (opcional): ")

        cursor.execute("""
        INSERT INTO Produtos (nome, codigo, preco, data_validade, descricao) 
        VALUES (%s, %s, %s, %s, %s)
        """, (nome, codigo, preco, data_validade, descricao))

    # Inserir dois registros em um único comando
    nome1 = input("Digite o nome do primeiro produto: ")
    codigo1 = input("Digite o código do primeiro produto (único): ")
    preco1 = float(input("Digite o preço do primeiro produto: "))
    data_validade1 = input("Digite a data de validade do primeiro produto (YYYY-MM-DD): ")
    descricao1 = input("Digite uma descrição do primeiro produto (opcional): ")

    nome2 = input("Digite o nome do segundo produto: ")
    codigo2 = input("Digite o código do segundo produto (único): ")
    preco2 = float(input("Digite o preço do segundo produto: "))
    data_validade2 = input("Digite a data de validade do segundo produto (YYYY-MM-DD): ")
    descricao2 = input("Digite uma descrição do segundo produto (opcional): ")

    cursor.execute("""
    INSERT INTO Produtos (nome, codigo, preco, data_validade, descricao) 
    VALUES (%s, %s, %s, %s, %s), (%s, %s, %s, %s, %s)
    """, (nome1, codigo1, preco1, data_validade1, descricao1, 
          nome2, codigo2, preco2, data_validade2, descricao2))

    # Confirmar as inserções
    connection.commit()
    cursor.close()
    connection.close()

def consultar_dados():
    connection = mysql.connector.connect(
        host='localhost',
        user='vrsmarcos26',
        password='12345',  
        database='ExemploDB'
    )

    cursor = connection.cursor()

    # Consulta
    filtro = input("Digite o valor que deseja pesquisar no nome do produto: ")

    cursor.execute("SELECT * FROM Produtos WHERE nome LIKE %s", (f"%{filtro}%",))
    resultados = cursor.fetchall()

    if not resultados:
        print("Tabela vazia.")
    else:
        # Mostrar na horizontal
        print("\nResultados na Horizontal:")
        for row in resultados:
            print(" | ".join(map(str, row)))

        # Mostrar na vertical
        print("\nResultados na Vertical:")
        for row in resultados:
            for index, col in enumerate(row):
                print(f"Coluna {index + 1}: {col}")

    cursor.close()
    connection.close()

def apagar_registro():
    connection = mysql.connector.connect(
        host='localhost',
        user='vrsmarcos26',
        password='12345', 
        database='ExemploDB'
    )

    cursor = connection.cursor()

    # Apagar registro
    codigo_para_deletar = input("Digite o código do produto que deseja apagar: ")

    cursor.execute("DELETE FROM Produtos WHERE codigo = %s", (codigo_para_deletar,))

    # Confirmar a exclusão
    connection.commit()

    if cursor.rowcount == 0:
        print("Nenhum registro encontrado com esse código.")
    else:
        print("Registro apagado com sucesso.")

    cursor.close()
    connection.close()

def main():
    criar_banco_e_tabela()
    inserir_dados()
    consultar_dados()
    apagar_registro()

if __name__ == "__main__":
    main()
