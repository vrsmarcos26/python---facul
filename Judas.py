#empacotamento e desempacotamento de parametros

def soma (*valor): #funções -----
    r = 0
    for i in valor:
        r += i
    return r

def exibeforma(a,b,c):
    print("1. valor = {} ".format(a))
    print("2. valor = {} ".format(b))
    print("3. valor = {} ".format(c))

def returnMult (x,y):
    ad = x + y
    su = x - y
    mu = x * y
    dv = x / y
    return(ad,su,mu,dv)

#----- FATORIAL -----

def fatorial (n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1)

def somaLista(L): # ------= soma a lista de forma recursiva------
    print (L)
    if L ==[]:
        return 0
    else:
        return L[0] + somaLista(L[1:])

#DocString 
x = 10
print()

def escopo():
    y = x * 2
    print("x global existe fora da funcao {}")


#soma ----

print(soma(3,9))
print(soma(1,2,3,4))

#--- empacotamento ---
L = [31,77,193]
exibeforma(*L)



#------0 retorna multiplos valores -------
a = 4
b = 6
s = returnMult(a,b)
print("Resultados {}".format(s))

print(fatorial(5))
l = [1,2,3,4,5,6,7,8,9]
print(somaLista(l))

-- Estado
CREATE TABLE Estado (
    ID INT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL
);

-- Município
CREATE TABLE Municipio (
    ID INT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Populacao INT,
    EstadoID INT,
    FOREIGN KEY (EstadoID) REFERENCES Estado(ID)
);

-- Pessoa (Cliente)
CREATE TABLE Pessoa (
    ID INT PRIMARY KEY,
    NomeCompleto VARCHAR(255) NOT NULL,
    DataNascimento DATE,
    CPF VARCHAR(14),
    Sexo CHAR(1),
    Status VARCHAR(50)
);

-- Teste
CREATE TABLE Teste (
    ID INT PRIMARY KEY,
    PessoaID INT,
    Data DATE,
    Resultado VARCHAR(50),
    MunicipioID INT,
    FOREIGN KEY (PessoaID) REFERENCES Pessoa(ID),
    FOREIGN KEY (MunicipioID) REFERENCES Municipio(ID)
);

-- Histórico de Taxas
CREATE TABLE HistoricoTaxaRecuperacao (
    ID INT PRIMARY KEY,
    MunicipioID INT,
    Data DATE,
    PorcentagemInfectados DECIMAL(5, 2),
    FOREIGN KEY (MunicipioID) REFERENCES Municipio(ID)
);

-- Vacina
CREATE TABLE Vacina (
    ID INT PRIMARY KEY,
    Nome VARCHAR(255),
    Empresa VARCHAR(255),
    DataFabricacao DATE,
    Lote VARCHAR(255)
);

-- Tipo de Vacina
CREATE TABLE TipoVacina (
    ID INT PRIMARY KEY,
    Funcao VARCHAR(255),
    Doses INT
);

-- Associação Vacina-Tipo de Vacina
CREATE TABLE Vacina_Tipo (
    VacinaID INT,
    TipoID INT,
    FOREIGN KEY (VacinaID) REFERENCES Vacina(ID),
    FOREIGN KEY (TipoID) REFERENCES TipoVacina(ID),
    PRIMARY KEY (VacinaID, TipoID)
);

-- Administração de Vacina
CREATE TABLE AdministracaoVacina (
    ID INT PRIMARY KEY,
    PessoaID INT,
    VacinaID INT,
    DataAdministracao DATE,
    DosesAdministradas INT,
    FOREIGN KEY (PessoaID) REFERENCES Pessoa(ID),
    FOREIGN KEY (VacinaID) REFERENCES Vacina(ID)
);

-- Aquisição
CREATE TABLE Aquisicao (
    ID INT PRIMARY KEY,
    MunicipioID INT,
    VacinaID INT,
    DataAquisicao DATE,
    Quantidade INT,
    FOREIGN KEY (MunicipioID) REFERENCES Municipio(ID),
    FOREIGN KEY (VacinaID) REFERENCES Vacina(ID)
);
