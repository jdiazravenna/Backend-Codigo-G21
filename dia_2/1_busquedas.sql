select * from alumnos where email like '%gmail.com'; --> % hace que no importe lo q esté adelante para buscar
select * from alumnos where email ilike '%gmail.com'; --> insensible a mayusculas
select * from alumnos where email like '%gmail.com%'; --> busca la palabra donde se encuentre

--> buscar alumnos donde en el nombre tenda la segunda letra, A
select * from alumnos where nombre ilike '_a%';

--> Mostrar todos los alumnos cuyo nombre tengan en la cuarta posicion la letra i y q terminen con la letra r
select * from alumnos where nombre ilike '___i%r';

--> ordenar los alumnos de manera ascendente ASC o descendente DESC
select * from alumnos order by nombre asc;
select * from alumnos order by nombre desc;

--> Actualizacion

update alumnos set nombre = 'Juanita', apellidos = 'Perez' where id = 1;

--> Eliminacion

delete from alumnos where id = 1;