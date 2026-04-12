create database perkal;

use perkal;

create table cliente(

	id_cli int not null auto_increment,

    nome varchar(100) not null,

    cpf char(11) not null,

    fone char(11) not null,

    cidade varchar(100),

    primary key (id_cli)

);
 
insert into cliente(nome,cpf,fone,cidade)

values("CARLOS HAGAMENON","456783232","67999999999","CG");
 
insert into cliente(nome, cpf, fone, cidade)

values("ELIANDRO","77777777777","67333333333","SP");
 
select * from cliente;

show tables;
 
update cliente set nome = "Luan Sales"

where id_cli = 3;
 
create table carro(

	id_car int not null auto_increment,

    marca varchar (50) not null,

    modelo varchar (50) not null,

    primary key (id_car)

);
 
insert into carro(marca, modelo)

values("Fiat","Uno");
 
insert into carro(marca, modelo)

values("Hyundai","HB20");
 
select * from carro;
 