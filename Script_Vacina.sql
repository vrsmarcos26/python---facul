-- Estado
CREATE TABLE ESTADO (
    id_estado INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

-- Município
CREATE TABLE MUNICIPIO (
    id_municipio INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    populacao INT,
    id_estado INT,
    FOREIGN KEY (id_estado) REFERENCES ESTADO(id_estado),
    id_estado PRIMARY KEY
);

-- Pessoa (Cliente)
CREATE TABLE PESSOA (
    cpf INT PRIMARY KEY,
    nome_completo VARCHAR(255) NOT NULL,
    data_nascimento DATE,
    rg int,
    sexo CHAR(1),
    Status VARCHAR(50)
);

-- Teste
CREATE TABLE TESTE (
    id_teste INT PRIMARY KEY,
    id_pessoa INT,
    Data DATE,
    resultado VARCHAR(50),
    id_municipio INT,
    FOREIGN KEY (id_pessoa) REFERENCES PESSOA(cpf),
    FOREIGN KEY (id_municipio) REFERENCES MUNICIPIO(id_municipio)
);

-- Histórico de Taxas
CREATE TABLE HISTORICO_TAXA_RECUPERACAO (
    id_data INT PRIMARY KEY,
    id_municipio INT,
    Data DATE,
    porcentagem_infectados DECIMAL(5, 2),
    FOREIGN KEY (id_municipio) REFERENCES MUNICIPIO(id_municipio),
    id_municipio PRIMARY KEY
);

-- Vacina
CREATE TABLE VACINA (
    id_vacina INT PRIMARY KEY,
    nome VARCHAR(255),
    empresa VARCHAR(255),
    data_fabricacao DATE,
    lote VARCHAR(255)
);

-- Tipo de Vacina
CREATE TABLE TIPO_VACINA (
    id INT,
    funcao VARCHAR(255),
    doses INT
);

-- Associação Vacina-Tipo de Vacina
CREATE TABLE VACINA_TIPO (
    id_vacina INT,
    id_tipo INT,
    FOREIGN KEY (id_vacina) REFERENCES VACINA(id_vacina),
    FOREIGN KEY (id_tipo) REFERENCES TipoVacina(id),
    PRIMARY KEY (id_vacina, id_tipo)
);

-- Administração de Vacina
CREATE TABLE ADMINISTRACAO_VACINA (
    id_administracao INT PRIMARY KEY,
    id_pessoa INT,
    id_vacina INT,
    data_administracao DATE,
    doses_administradas INT,
    FOREIGN KEY (id_pessoa) REFERENCES PESSOA(id_pessoa),
    FOREIGN KEY (id_vacina) REFERENCES VACINA(id_vacina)
);

-- Aquisição
CREATE TABLE AQUISICAO (
    id_aquisicao INT PRIMARY KEY,
    id_municipio INT,
    id_vacina INT,
    data_aquisicao DATE,
    quantidade INT,
    FOREIGN KEY (id_municipio) REFERENCES MUNICIPIO(id_municipio),
    FOREIGN KEY (id_vacina) REFERENCES VACINA(id_vacina)
);
