--> Así se puede obtener la informacion de dos tablas relacionadas entre si
select * from clientes inner join cuentas on clientes.id = cuentas.cliente_id;

--> para declarar un left join que seria de manera obligatoria todo lo de la izquierda y opcionalemnte lo de la derecha

SELECT * FROM clientes LEFT JOIN cuentas ON cuentas.cliente_id = clientes.id;

--> para declarar un right join que seria de manera obligatoria todo lo de la derecha y opcionalemnte lo de la izquierda
SELECT * FROM cuentas LEFT JOIN clientes ON cuentas.cliente_id = clientes.id;

--> Tenemos que declarar la tabla de la columna si vamos a seleccionar una columna que es ambigua en las 2 tablas
SELECT clientes.id, clientes.nombre, cuentas.id, cuentas.numero_cuenta FROM clientes LEFT JOIN cuentas ON clientes.id = cuentas.cliente_id;

--> ademas podemos agregar un alias a nuestra tabla para hacer mas corta en su nombre
SELECT cli.id, cli.nombre, cue.id, cue.numero_cuenta FROM clientes AS cli LEFT JOIN cuentas AS cue ON cli.id=cue.cliente_id; 

-- Ejercicios

-- devolver la informacion(nombre, correo, status, numero_cuenta, tipo_cuenta)
select clientes.nombre, clientes.correo, clientes.status, cuentas.numero_cuenta, cuentas.tipo_moneda 
from clientes 
    inner join cuentas on clientes.id=cuentas.cliente_id;
-- devolver la informacion de los usuarios que tengan cuenta que no sea en soles (solo quiero el nombre y correo)
select clientes.nombre, clientes.correo 
from clientes 
    inner join cuentas on clientes.id = cuentas.cliente_id where cuentas.tipo_moneda != 'SOLES';
-- Devolver el nombre, mantenimiento y tipo_moneda
select clientes.nombre, cuentas.mantenimiento, cuentas.tipo_moneda 
from clientes 
    inner join cuentas on clientes.id = cuentas.cliente_id;
-- Devolver el usuario (correo, nombre) y el tipo_moneda de los usuarios qye tenan correo gmail y que su mantenimiento sea menos que 1.1 y que el usuario este activo
select clientes.correo, clientes.nombre from clientes inner join cuentas on clientes.id=cuentas.cliente_id
where clientes.correo like '%gmail.com' and cuentas.mantenimiento < '1.1' and clientes.activo= 'TRUE';

--> devolver cuantos clientes no tienen cuentas
select count(*) from clientes left join cuentas  on cliientes.id = cuentas.cliente_id where cuentas.numero_cuenta is null;

create table movimientos(
    id serial primary key not null,
    cuenta_origen int,
    cuenta_destino int not null,
    monto float not null,
    fecha_operacion TIMESTAMP default now(),
    --relaciones
    CONSTRAINT fk_cuenta_origen FOREIGN key(cuenta_origen) references cuentas(id),
    CONSTRAINT fk_cuenta_destino FOREIGN key(cuenta_destino) references cuentas(id)
    );
alter table movimientos alter column cuenta_destino drop not null;

INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
(null, 1, 100.10, '2024-07-01T14:15:17'),
(null, 2, 500.20, '2024-07-06T09:30:15'),
(null, 3, 650.00, '2024-07-06T15:29:18'),
(null, 4, 456.00, '2024-07-08T10:15:17'),
(null, 5, 500.00, '2024-07-10T17:18:24'),
(null, 6, 1050.24, '2024-07-04T12:12:12'),
(null, 7, 984.78, '2024-07-09TT11:06:49'),
(1,2, 40.30, '2024-07-10T10:10:10'),
(4,7, 350.00, '2024-07-16T20:15:35'),
(3, null, 50.00, '2024-07-16T22:15:10'),
(5, null, 100.00, '2024-07-17T10:19:25'),
(6, null, 350.28, '2024-07-18T14:15:16');

select case
when activo is TRUE then 'ESTA ACTIVO EL CLIENTE'
WHEN ACTIVO IS FALSE THEN 'EL CLIENTE NO PUEDE HACER OPERACIONES'
ELSE 'HUBO UN ERROR'
END,
ACTIVO FROM CLIENTES;

-- Usando el switch case Mostrar los movimientos que sean DEPOSITO, TRANSFERENCIA o RETIRO, siendo:
-- DEPOSITO: Cuando no hay cuenta_origen pero si cuenta destino
-- TRANSFERENCIA: Cuando hay cuenta_origen y cuenta_destino
-- RETIRO : Cuando hay cuenta_origen y no hay cuenta_destino
-- y sus montos

SELECT CASE 
WHEN cuenta_origen IS NULL AND cuenta_destino IS NOT NULL THEN 'DEPOSITO'
WHEN cuenta_origen IS NOT NULL AND cuenta_destino IS NOT NULL THEN 'TRANSFERENCIA'
ELSE 'RETIRO'
END,
MONTO FROM MOVIMIENTOS;

-- En base al correo de los clientes hacer lo siguiente

-- Si el correo es gmail > 'ES UNA PERSONA JOVEN'
-- Si el correo es hotmail > 'ES UNA PERSONA ADULTA'
-- Si el correo es yahoo > 'ES UN DINOSAURIO'
-- PISTA: Usar el like en el 
SELECT CASE 
WHEN correo like '%gmail%' THEN 'ES UNA PERSONA JOVEN'
WHEN correo like '%hotmail%' THEN 'ES UNA PERSONA ADULTA'
WHEN correo like '%yahoo%' THEN 'ES UN DINOSAURIO'
END,
correo
FROM CLIENTES;


-- Usando la funcion de agregacion SUM obtener los debitos de todas cuenta (lo que sale) cuenta_origen NO ES NULA
select cuenta_origen, sum(monto)
from movimientos where cuenta_origen is not null group by  cuenta_origen;

-- Obtener los creditos de todas las cuentas (lo que llega / entra) > cuanta_destino NO ES NULA

select cuenta_destino, sum(monto)
from movimientos where cuenta_destino is not null group by cuenta_destino;