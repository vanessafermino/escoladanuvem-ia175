-- Criando a tabela Cliente
CREATE TABLE Cliente (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  contato VARCHAR(100),
  endereco VARCHAR(255)
);

-- Criando a tabela Veiculo
CREATE TABLE Veiculo (
  chassi VARCHAR(20) PRIMARY KEY,
  modelo VARCHAR(50),
  marca VARCHAR(50),
  ano INT,
  cliente INT,
  FOREIGN KEY (cliente) REFERENCES Cliente(id)
);

-- Criando a tabela Mecanico
CREATE TABLE Mecanico (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100),
  especialidade VARCHAR(100)
);

-- Criando a tabela OrdemServico
CREATE TABLE OrdemServico (
  numero INT PRIMARY KEY AUTO_INCREMENT,
  dataEmissao DATE,
  dataConclusao DATE,
  status VARCHAR(20),
  valorTotal DECIMAL(10,2),
  veiculo VARCHAR(20),
  FOREIGN KEY (veiculo) REFERENCES Veiculo(chassi)
);

-- Criando a tabela Servico
CREATE TABLE Servico (
  id INT PRIMARY KEY AUTO_INCREMENT,
  descricao VARCHAR(255)
);

-- Criando a tabela Peca
CREATE TABLE Peca (
  id INT PRIMARY KEY AUTO_INCREMENT,
  descricao VARCHAR(255),
  valorUnitario DECIMAL(10,2)
);

-- Criando a tabela TabelaPreco
CREATE TABLE TabelaPreco (
  id INT PRIMARY KEY AUTO_INCREMENT,
  servico INT,
  valorMaoDeObra DECIMAL(10,2),
  FOREIGN KEY (servico) REFERENCES Servico(id)
);

-- Criando a tabela OS_Tem_Servico
CREATE TABLE OS_Tem_Servico (
  os_numero INT,
  servico_codigo INT,
  quantidade INT,
  PRIMARY KEY (os_numero, servico_codigo),
  FOREIGN KEY (os_numero) REFERENCES OrdemServico(numero),
  FOREIGN KEY (servico_codigo) REFERENCES Servico(id)
);

-- Criando a tabela OS_Utiliza_Peca
CREATE TABLE OS_Utiliza_Peca (
  os_numero INT,
  peca_codigo INT,
  quantidade INT,
  PRIMARY KEY (os_numero, peca_codigo),
  FOREIGN KEY (os_numero) REFERENCES OrdemServico(numero),
  FOREIGN KEY (peca_codigo) REFERENCES Peca(id)
);