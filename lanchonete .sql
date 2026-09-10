create database lanchonete;
use lanchonete;

create table clientes (telefone varchar(11) primary key not null,
nome varchar (50) not null,
cidade varchar(50) not null);

create table produtos (id_pdt int auto_increment primary key,
nome_produto varchar(50),
categoria varchar(50),
preco int);

create table tabela_pedidos (id_tp int auto_increment primary key,
telefone varchar(11),
id_pdt int,
data_pedido date,
foreign key (telefone) references clientes(telefone),
foreign key (id_pdt) references produtos(id_pdt));

insert into clientes (nome, telefone, cidade) values
("Pedro Henrique","21999998888","Rio de Janeiro"),
("Marcelo Silva","21988887777","Niterói"),
("Ana Beatriz","21977776666","Rio de Janeiro"),
("Carla Souza","21966665555","São Gonçalo");

select * from clientes;

insert into produtos (nome_produto, categoria, preco) values
("X-Burguer Especial","Lanche",22.50),
("Batata Frita Média","Acompanhamento",12.00),
("Suco Natural de Laranja","Bebida", 8.50),
("Refrigerante Lata","Bebida",6.00),
("Milkshake de Chocolate","Sobremesa",15.00);

select * from produtos;

insert into tabela_pedidos (telefone, id_pdt, data_pedido) values
("21999998888",1,"2026-08-28"),
("21999998888",4,"2026-08-28"),
("21988887777",1,"2026-08-29"),
("21988887777",2,"2026-08-29"),
("21977776666",5,"2026-08-28"),
("21966665555",3,"2026-08-28");

select * from tabela_pedidos;

select * from clientes where cidade = "Rio de Janeiro";

select * from produtos where preco > 10;

