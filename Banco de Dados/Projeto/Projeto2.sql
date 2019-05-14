create table Cliente(
	Id_Cliente smallint primary key,
	Nome varchar(60) not null,
)

create table Juridico(
	CNPJ varchar(14) unique,
	Id_Cliente smallint primary key constraint fk_Id_Cliente_Juridico foreign key(Id_Cliente) references Cliente
)

create table Fisico(
	CPF varchar(11) constraint ck_CPF_Fisico check(len(CPF)=11) unique,
	Id_Cliente smallint primary key constraint fk_Id_Cliente_Fisico foreign key(Id_Cliente) references Cliente
)

create table Entregador(
	CNH varchar(20) not null unique,
	Nome varchar(45) not null,
	Id_Entregador smallint primary key
)

create table Pagamento(
	Id_Pagamento smallint primary key,
	Tipo_Pagamento varchar(25),
	DataPag date not null,
	Valor smallmoney not null
)

create table Pratos(
	Id_Pratos smallint primary key,
	Restricao varchar(30) default 'Sem restrição',
)

create table Pedido(
	Id_Pedido smallint primary key,
	Brinde varchar(20) default 'Sem brinde',
	Hora time,
	DataPed date not null,
	Rua varchar(25) not null,
	Numero smallint not null,
	ValorEntrega smallmoney,
	Id_Entregador smallint constraint fk_Id_Entregador foreign key (Id_Entregador) references Entregador,
	Id_Pratos smallint constraint fk_Id_Pratos foreign key (Id_Pratos) references Pratos,
	Id_Pagamento smallint constraint fk_Id_Pagamento foreign key (Id_Pagamento) references Pagamento,
	Id_Cliente smallint constraint fk_Id_Cliente foreign key (Id_cliente references Cliente),
	primary key (Id_Pedido, Id_Entregador, Id_Pratos, Id_Pagamento, Id_Cliente)
)

create table Ingredientes(
	Id_Ingrediente smallint primary key,
	Valor smallmoney,
	Nome varchar(20) not null
)

create table Tem(
	Id_Ingrediente smallint constraint fk_Id_Ingrediente_Tem foreign key (Id_Ingrediente) references Ingredientes,
	Id_Pratos smallint constraint fk_Id_Pratos_Tem foreign key (Id_Pratos) references Pratos,
	primary key (Id_Pratos, Id_Ingrediente)
)

create table Opcao1(
	Id_Pratos smallint constraint fk_Id_Pratos_Opcao1 foreign key (Id_Pratos) references Pratos,
	PratoUnico varchar(20),
	primary key (Id_Pratos)
)

create table Opcao2(
	Id_Pratos smallint constraint fk_Id_Pratos_Opcao2 foreign key (Id_Pratos) references Pratos,
	Proteina varchar(15),
	PrimeiraOp varchar(20),
	SegundaOp varchar(20),
	primary key (Id_Pratos)
)

create table Telefone(
	Id_Cliente smallint constraint fk_Id_Cliente_Telefone foreign key (Id_Cliente) references Cliente,
	Telefone varchar(11) not null
)