create table if not exists Sotrudnik (
id serial primary key,
FIO varchar(100) unique not null,
department varchar(40) not null,
boss_id integer
);