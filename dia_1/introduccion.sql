-- psql -U USUARIO -h HOSTNAME -p PUERTO NOMBRE_BD -> conexion mas exacta para conextarnos a la BD

--Así se define un comentario en BD
-- DDL Data Definition Langueja, es un sub lenguaje de sql para definir como se almacenaran los datos

create database pruebas;

--\cls -> limpiará la terminal
-- \c pruebas -> conecta a la BD pruebas creada
create table alumnos(
    id serial not null primary key, -- columna q sera autoincrementable, no puede ser nula y llave será primeria
    nombre text not null, -- sera texto y no puede ser nula
    email text not null unique, -- sera texto, no puede ser nula y debe ser unica (no se repite)
    matriculado boolean default true, -- sera booleano
    fecha_nacimiento date null
);

-- Para agregar columnas a una tabla ya existente
alter table alumnos apellidos text;

-- Para cambiar el tipo de dato de un elemento
-- solo se puede cambiar el tipo de dato si la columna no tiene registros
-- o si ya tiene registros, entonces el nuevo tipo de datos, debe ser compatible con el antiguo
-- no podemos cambiar de un TEXT > INT o de un INT > DATE
alter table alumnos alter column nombre type varchar(100);

-- Para eliminar una tabla de manera permanente e irreversible y toda la informacion q hay en ella
drop table direcciones;
drop database nombre_BD;

-- DML (Data manipulation languaje)
-- es un sublenguaje para pode interactuar con la informacion de las tablas

-- alter table alumnos add constraint alumnos_nombre_key unique(nombre); (añade una constraint)

-- insertamos 3 registros en la tabla Alumnos
insert into alumnos values
(default, 'cesar', 'ccenteno@tecsup.edu.pe', default, '1995-06-02', 'centeno'),
(default, 'javier', 'jwiesse@gmail.com', false, '2000-02-14', 'wiesse'), 
(default, 'farit', 'fatir@gmail.com', true, '2001-05-15', 'Espinoza');

-- Para seleccionar ciertos registros donde Matriculado sea False
select * from alumnos where matriculado = false;

-- Para seleccionar la columna nombre de la tabla
select nombre from alumnos;

-- Para seleccionar todos los datos de la tabla
select * from alumnos;

-- Para seleccionar 2 columnas de la tabla alumnos
select id, nombre from alumnos;

-- Para seleccionar datos con doble condicion, ambas deben ser verdaderas
select * from alumnos where matriculado = true and id < 3;

-- Para seleccionar datos con doble condicion, una de ellas debe ser verdadera
select * from alumnos where matriculado = true or id <3;

-- Devolver todos los alumnos que estén matriculados y que su fecha de nacimiento sea mayor al 01-01-1995

select * from alumnos where matriculado = true and fecha_nacimiento > '1995-01-01';

select * from alumnos where email like '%gmail.com';
select * from alumnos where email ilike '%gmail.com'; --> insensible a mayusculas
