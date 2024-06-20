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
    id_estado INT PRIMARY KEY,
    FOREIGN KEY (id_estado) REFERENCES ESTADO(id_estado)
);

-- Pessoa (Cliente)
CREATE TABLE PESSOA (
    cpf INT PRIMARY KEY,
    nome_completo VARCHAR(255) NOT NULL,
    data_nascimento DATE,
    rg INT,
    sexo CHAR(1)
);

-- Teste
CREATE TABLE TESTE (
    id_teste INT PRIMARY KEY,
    cpf INT,
    data DATE,
    resultado VARCHAR(50),
    id_municipio INT,
    FOREIGN KEY (cpf) REFERENCES PESSOA(cpf),
    FOREIGN KEY (id_municipio) REFERENCES MUNICIPIO(id_municipio)
);

-- Histórico de Taxas
CREATE TABLE HISTORICO_TAXA_RECUPERACAO (
    id_data INT,
    id_municipio INT,
    data DATE,
    porcentagem_infectados DECIMAL(5, 2),
    PRIMARY KEY (id_data, id_municipio),
    FOREIGN KEY (id_municipio) REFERENCES MUNICIPIO(id_municipio)
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
CREATE TABLE VACINA_TIPO (
    id_vacina INT,
    id_tipo INT,
    FOREIGN KEY (id_vacina) REFERENCES VACINA(id_vacina),
    PRIMARY KEY (id_vacina, id_tipo)
);

-- Administração de Vacina
CREATE TABLE ADMINISTRACAO_VACINA (
    id_administracao INT,
    cpf INT,
    id_vacina INT,
    data_administracao DATE,
    doses_administradas INT,
    FOREIGN KEY (cpf) REFERENCES PESSOA(cpf),
    FOREIGN KEY (id_vacina) REFERENCES VACINA(id_vacina)
    PRIMARY KEY (cpf, id_vacina, id_administracao),
);

-- Aquisição
CREATE TABLE AQUISICAO (
    id_aquisicao INT,
    id_municipio INT,
    id_vacina INT,
    data_aquisicao DATE,
    quantidade INT,
    FOREIGN KEY (id_municipio) REFERENCES MUNICIPIO(id_municipio),
    FOREIGN KEY (id_vacina) REFERENCES VACINA(id_vacina)
    PRIMARY KEY (id_aquisicao, id_municipio, id_vacina),
);
