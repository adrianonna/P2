create database bd_Lolla
--on primary(
--name = bd_Lolla,
--filename = 'C:\Users\Adriano\Google Drive\Coisas TSI\Banco de dados\Projeto\bd_Lolla.mdf',
--size = 20mb,
--maxsize = 200mb,
--filegrowth = 10% 
--)
go
use bd_Lolla
go

create table Cliente(
Id_Cliente smallint primary key,
Nome varchar(60) not null,
Rua varchar(40) not null,
Numero smallint not null,
Telefone varchar(15) not null,
Telefone2 varchar(15)
)

create table Mesa(
Id_Mesa smallint primary key,
Qtde_Pessoa smallint constraint ck_Qtde_Pessoa_Mesa check (Qtde_Pessoa < 5),
Hora time,
Dia date,
Id_Cliente smallint constraint fk_Id_Cliente_Mesa foreign key (Id_Cliente) references Cliente
)

create table Juridico(
CNPJ varchar(14) unique,
Id_Cliente smallint primary key constraint fk_Id_Cliente_Juridico foreign key(Id_Cliente) references Cliente
)

create table Fisico(
CPF varchar(11) constraint ck_CPF_Fisico check(len(CPF)=11),
Id_Cliente smallint primary key constraint fk_Id_Cliente_Fisico foreign key(Id_Cliente) references Cliente
)

create table Funcionario(
Id_Funcionario smallint primary key,
Salario smallmoney constraint ck_Salario_Funcionario check(Salario > 988 and Salario < 2000) not null,
Idade tinyint check (Idade > 18),
Genero varchar(1) constraint ck_Genero_Funcionario check(Genero in ('M', 'F')),
Nome varchar(60) not null,
CidadeNascimento varchar(20) default 'João Pessoa',
Id_FuncGerenciado smallint constraint fk_Id_FuncGerenciado foreign key (Id_FuncGerenciado) references Funcionario
)

create table Entregador(
CNH varchar(20) not null unique,
Id_Funcionario smallint constraint fk_Id_Funcionario_Entregador foreign key (Id_Funcionario) references Funcionario,
primary key (Id_Funcionario)
)

create table Dependente(
Id_Dependente smallint primary key,
Nome varchar(60),
Beneficio varchar(30),
Id_Funcionario smallint constraint fk_Id_Funcionario_Dependente foreign key (Id_Funcionario) references Funcionario
)

create table Pagamento(
Id_Pagamento smallint primary key,
Tipo_Pagamento varchar(20),
Dia date not null,
Valor smallmoney not null
)

create table Pedido(
Id_Pedido smallint primary key,
Brinde varchar(20)
)

create table Efetua(
Id_Pedido smallint constraint fk_Id_Pedido_Efetua foreign key (Id_Pedido) references Pedido,
Id_Cliente smallint constraint fk_Id_Cliente_Efetua foreign key (Id_Cliente) references Cliente,
Id_Pagamento smallint constraint fk_Id_Pagamento_Efetua foreign key (Id_Pagamento) references Pagamento,
primary key (Id_Cliente, Id_Pedido)
)

create table Pratos(
Id_Pratos smallint primary key,
Restricao varchar(30) default 'Sem restrição',
)

create table PedidoPrato(
Id_Pedido smallint constraint fk_Id_Pedido_PedidoPrato foreign key (Id_Pedido) references Pedido,
Id_Pratos smallint constraint fk_Id_Pratos_PedidoPrato foreign key (Id_Pratos) references Pratos,
primary key (Id_Pedido, Id_Pratos)
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

create table Entrega(
Id_Pratos smallint constraint fk_Id_Pratos_Entrega foreign key (Id_Pratos) references Pratos,
Id_Pedido smallint constraint fk_Id_Pedido_Entrega foreign key (Id_Pedido) references Pedido,
Id_Funcionario smallint constraint fk_Id_Funcionario_Entrega foreign key (Id_Funcionario) references Funcionario,
ValorEntrega smallmoney,
primary key (Id_Pratos, Id_Pedido)
)

alter table Mesa
add Id_Funcionario_Garcom_Atende smallint constraint fk_Id_Funcionario_Garcom_Atende_Mesa foreign key(Id_Funcionario_Garcom_Atende) references Funcionario

insert into Cliente (Nome, Rua, Numero, Telefone, Telefone2)
values ('Adriano Ney Nascimento do Amaral', 'Golfo de Coronation', '150', '83987809422', '83999391645')

insert into Cliente (Nome, Rua, Numero, Telefone, Telefone2)
values ('Paolla Duarte', 'Cristovão Colombo', '15', '83987804136', default)

insert into Cliente (Nome, Rua, Numero, Telefone, Telefone2)
values ('Martha Duarte', 'Cristovão Colombo', '15', '83987808888', default)

insert into Cliente (Nome, Rua, Numero, Telefone, Telefone2)
values ('Paulo Roberto', 'Cristovão Colombo', '15', '83987809999', default)

insert into Cliente (Nome, Rua, Numero, Telefone, Telefone2)
values ('Bruno Silva', 'Francisco Moura', '482', '83987807777', default)

insert into Cliente (Nome, Rua, Numero, Telefone, Telefone2)
values ('Bruna Silvo', 'Francisco Moura', '482', '83987807777', default)

insert into Funcionario (Salario, Idade, Genero, Nome, CidadeNascimento, Id_FuncGerenciado)
values ('1000', '20', 'M', 'Pedro Alves', default, default)

insert into Mesa (Qtde_Pessoa, Hora, Dia, Id_Cliente)
values ('4', '11:00:00', '2018-08-07', 3)

insert into Mesa (Qtde_Pessoa, Hora, Dia, Id_Cliente)
values ('2', '12:00:00', '2018-08-10', 2)

insert into Fisico (CPF, Id_Cliente)
values ('01136425470', 3)

insert into Fisico (CPF, Id_Cliente)
values ('12345678910', 2)

insert into Fisico (CPF, Id_Cliente)
values ('12345674567', 1)

insert into Juridico(CNPJ, Id_Cliente)
values ('12345674567236', 4)

insert into Juridico(CNPJ, Id_Cliente)
values ('20345674247236', 5)

insert into Fisico(CPF, Id_Cliente)
values ('15647352856', 6)







select * from Cliente

select *
from Cliente
join Mesa
on cliente.Id_Cliente = Mesa.Id_Cliente


