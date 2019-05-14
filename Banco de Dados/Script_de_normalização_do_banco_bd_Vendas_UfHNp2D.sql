USE bd_Vendas
GO

-- Aplicar 1FN na tabela Pedido1 e eliminar as tabelas aninhadas
-- Os itens do pedido estão aninhados dentro de Pedido1 (multivalorado)
-- Criar a tabela Itens com os atributos multivalorados
SELECT idpedido, idproduto, nomeprod, precoprod, quantest, precovendido, quantvendida, valoritem
INTO Itens
FROM Venda

-- Excluir os atributos multivalorados da tabela Venda
ALTER TABLE Venda 
DROP COLUMN idproduto, nomeprod, precoprod, quantest, precovendido, quantvendida, valoritem

-- Excluir as linhas repetidas da tabela Venda
SELECT DISTINCT *
INTO Pedido
FROM Venda

-- Excluir a tabela Venda
DROP TABLE Venda

-- Definir a chave primária da tabela Pedido
ALTER TABLE Pedido ADD CONSTRAINT PK_Pedido PRIMARY KEY (idpedido)

-- Definir a chave estrangeira da tabela Itens oriunda da tabela Pedido
ALTER TABLE Itens ADD CONSTRAINT FK_Itens_Pedido FOREIGN KEY (idpedido) REFERENCES Pedido

-- Definir a chave primária da tabela Itens
ALTER TABLE Itens ADD CONSTRAINT PK_Itens PRIMARY KEY (idpedido, idproduto)

-- As tabelas Pedido e Itens estão na 1FN
SELECT * FROM Pedido
SELECT * FROM Itens

-- Aplicar a 2FN na tabela Itens e eliminar a dependência parcial criando a tabela Produto
SELECT DISTINCT idproduto, nomeprod, precoprod, quantest
INTO Produto
FROM Itens

-- Definir a chave primária da tabela Produto
ALTER TABLE Produto ADD CONSTRAINT PK_Produto PRIMARY KEY (idproduto)

-- Excluir os atributos com dependência parcial da tabela Itens 
ALTER TABLE Itens DROP COLUMN nomeprod, precoprod, quantest

-- Definir a chave estrangeira na Tabela Itens oriunda da tabela Produto
ALTER TABLE Itens ADD CONSTRAINT FK_Itens_Produto FOREIGN KEY (idproduto) REFERENCES Produto

-- Todas as tabelas já estão na 2FN
SELECT * FROM Pedido
SELECT * FROM Itens
SELECT * FROM Produto

-- Aplicar a 3FN na tabela Itens

-- Aplicar a 3FN na tabela Pedido e criar a tabela Cliente
SELECT DISTINCT idcliente, nomecli, enderecocli, idcidade, nomecid, ufcid, idpais, nomepais
INTO Cliente
FROM Pedido

-- Definir a chave primária da tabela Cliente
ALTER TABLE Cliente ADD CONSTRAINT PK_cliente PRIMARY KEY (idcliente)

-- Aplicar a 3FN na tabela Pedido e criar a tabela Vendedor
SELECT DISTINCT idvendedor, nomevend, cpfvend, rgvend
INTO Vendedor
FROM Pedido

-- Definir a chave primária da tabela Vendedor
ALTER TABLE Vendedor ADD CONSTRAINT PK_Vendedor PRIMARY KEY (idvendedor)

-- Excluir os atributos com dependência transitiva da tabela Pedido
ALTER TABLE Pedido DROP COLUMN nomecli, enderecocli, idcidade, nomecid, ufcid, idpais, nomepais, nomevend, cpfvend, rgvend

-- Definir a chave estrangeira na tabela Pedido oriunda da tabela Cliente
ALTER TABLE Pedido ADD CONSTRAINT FK_Pedido_Cliente FOREIGN KEY (idcliente) REFERENCES Cliente

-- Definir a chave estrangeira da tabela Pedido oriunda da tabela Vendedor
ALTER TABLE Pedido ADD CONSTRAINT FK_Pedido_Vendedor FOREIGN KEY (idvendedor) REFERENCES Vendedor

-- Aplicar a 3FN na tabela Cliente e criar a tabela Cidade
SELECT DISTINCT idcidade, nomecid, ufcid, idpais, nomepais
INTO Cidade
FROM Cliente

-- Definir a chave primária da tabela Cidade
ALTER TABLE Cidade ADD CONSTRAINT PK_Cidade PRIMARY KEY (idcidade)

-- Eliminar os atributos com dependência transitiva de idcidade da tabela Cliente
ALTER TABLE Cliente DROP COLUMN nomecid, ufcid, idpais, nomepais

-- Definir a chave estrangeira na tabela Cliente oriunda da tabela CIDADE
ALTER TABLE Cliente ADD CONSTRAINT FK_Cliente_Cidade FOREIGN KEY (idcidade) REFERENCES Cidade

-- Aplicar a 3FN na tabela Cidade e criar a tabela Pais
SELECT DISTINCT idpais, nomepais
INTO Pais
FROM Cidade

-- Definir a chave primária da tabela Pais
ALTER TABLE Pais ADD CONSTRAINT PK_Pais PRIMARY KEY (idpais)

-- Eliminar os atributos com dependência transitiva de idpais da tabela Cidade
ALTER TABLE Cidade DROP COLUMN nomepais
SELECT * FROM Cidade

-- Definir a chave estrangeira da tabela Pais na tabela Cidade
ALTER TABLE Cidade ADD CONSTRAINT FK_Cidade_Pais FOREIGN KEY (idpais) REFERENCES Pais

-- Eliminar o atributo derivado valoritem
ALTER TABLE Itens DROP COLUMN valoritem

-- Todas as tabelas já estão na 3FN
SELECT * FROM Pedido
SELECT * FROM Itens
SELECT * FROM Produto
SELECT * FROM Cliente
SELECT * FROM Vendedor
SELECT * FROM Cidade
SELECT * FROM Pais